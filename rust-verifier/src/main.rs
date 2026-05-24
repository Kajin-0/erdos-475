use clap::Parser;
use serde::Deserialize;
use std::collections::{BTreeMap, BTreeSet, HashSet};
use std::fs::File;
use std::io::{BufRead, BufReader};

#[derive(Parser, Debug)]
#[command(author, version, about = "Independent minimal witness verifier for Erdős 475 finite certificates")]
struct Args {
    /// Minimal witness JSONL file.
    certificate: String,

    /// Expected domain such as 29:3-7 or 31:6. May repeat.
    #[arg(long = "domain")]
    domains: Vec<String>,

    /// Require B to be canonical under multiplicative scaling.
    #[arg(long)]
    require_canonical: bool,

    /// Require complete canonical coverage for declared domains.
    #[arg(long)]
    require_coverage: bool,
}

#[derive(Debug, Deserialize)]
struct Witness {
    p: u64,
    #[serde(rename = "B")]
    b: Vec<u64>,
    final_order: Vec<u64>,
}

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    if n == 2 || n == 3 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let mut f = 3u64;
    while f * f <= n {
        if n % f == 0 {
            return false;
        }
        f += 2;
    }
    true
}

fn canonical_scale(b: &[u64], p: u64) -> Vec<u64> {
    if b.is_empty() {
        return Vec::new();
    }
    let mut best: Option<Vec<u64>> = None;
    for lambda in 1..p {
        let mut scaled: Vec<u64> = b.iter().map(|x| (lambda * x) % p).collect();
        scaled.sort_unstable();
        match &best {
            Some(cur) if &scaled >= cur => {}
            _ => best = Some(scaled),
        }
    }
    best.unwrap()
}

fn combinations_rec(
    universe: &[u64],
    k: usize,
    start: usize,
    cur: &mut Vec<u64>,
    out: &mut BTreeSet<Vec<u64>>,
    p: u64,
) {
    if cur.len() == k {
        out.insert(canonical_scale(cur, p));
        return;
    }
    let need = k - cur.len();
    if universe.len() - start < need {
        return;
    }
    for idx in start..=universe.len() - need {
        cur.push(universe[idx]);
        combinations_rec(universe, k, idx + 1, cur, out, p);
        cur.pop();
    }
}

fn all_canonical_b(p: u64, k: usize) -> BTreeSet<Vec<u64>> {
    let universe: Vec<u64> = (1..p).collect();
    let mut out = BTreeSet::new();
    let mut cur = Vec::new();
    combinations_rec(&universe, k, 0, &mut cur, &mut out, p);
    out
}

fn parse_domain(text: &str) -> Result<(u64, Vec<usize>), String> {
    let (p_str, k_str) = text
        .split_once(':')
        .ok_or_else(|| format!("invalid domain format: {text}"))?;
    let p: u64 = p_str.parse().map_err(|_| format!("invalid p in domain: {text}"))?;
    if let Some((a, b)) = k_str.split_once('-') {
        let start: usize = a.parse().map_err(|_| format!("invalid k in domain: {text}"))?;
        let end: usize = b.parse().map_err(|_| format!("invalid k in domain: {text}"))?;
        if end < start {
            return Err(format!("invalid decreasing k range: {text}"));
        }
        Ok((p, (start..=end).collect()))
    } else {
        let k: usize = k_str.parse().map_err(|_| format!("invalid k in domain: {text}"))?;
        Ok((p, vec![k]))
    }
}

fn verify_witness(w: &Witness, line_no: usize, require_canonical: bool) -> Result<Vec<u64>, String> {
    let p = w.p;
    if !is_prime(p) {
        return Err(format!("line {line_no}: p={p} is not prime"));
    }

    let universe: BTreeSet<u64> = (1..p).collect();
    let mut b = w.b.clone();
    b.sort_unstable();

    let b_set: BTreeSet<u64> = b.iter().copied().collect();
    if b_set.len() != b.len() {
        return Err(format!("line {line_no}: B has duplicate entries"));
    }
    if !b_set.is_subset(&universe) {
        return Err(format!("line {line_no}: B is not a subset of F_p^*"));
    }
    if require_canonical && b != canonical_scale(&b, p) {
        return Err(format!("line {line_no}: B is not canonical under scaling: {:?}", b));
    }

    let a_set: BTreeSet<u64> = universe.difference(&b_set).copied().collect();
    let order_set: BTreeSet<u64> = w.final_order.iter().copied().collect();
    if order_set.len() != w.final_order.len() {
        return Err(format!("line {line_no}: final_order contains duplicates"));
    }
    if order_set != a_set {
        return Err(format!("line {line_no}: final_order is not F_p^* \\ B"));
    }

    let mut partials = HashSet::new();
    let mut s = 0u64;
    for &x in &w.final_order {
        s = (s + x) % p;
        if !partials.insert(s) {
            return Err(format!("line {line_no}: repeated nonempty partial sum {s}"));
        }
    }

    Ok(b)
}

fn main() -> Result<(), String> {
    let args = Args::parse();

    let file = File::open(&args.certificate)
        .map_err(|e| format!("failed to open {}: {e}", args.certificate))?;
    let reader = BufReader::new(file);

    let mut seen: BTreeMap<(u64, Vec<u64>), usize> = BTreeMap::new();
    let mut by_pk: BTreeMap<(u64, usize), BTreeSet<Vec<u64>>> = BTreeMap::new();
    let mut rows = 0usize;

    for (idx, line_result) in reader.lines().enumerate() {
        let line_no = idx + 1;
        let line = line_result.map_err(|e| format!("line {line_no}: read error: {e}"))?;
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }
        rows += 1;
        let witness: Witness = serde_json::from_str(trimmed)
            .map_err(|e| format!("line {line_no}: invalid JSON: {e}"))?;
        let b = verify_witness(&witness, line_no, args.require_canonical)?;
        let key = (witness.p, b.clone());
        if let Some(prev) = seen.insert(key, line_no) {
            return Err(format!("line {line_no}: duplicate witness; first seen at line {prev}"));
        }
        by_pk.entry((witness.p, b.len())).or_default().insert(b);
    }

    for domain in &args.domains {
        let (p, ks) = parse_domain(domain)?;
        for k in ks {
            let observed = by_pk.get(&(p, k)).cloned().unwrap_or_default();
            println!("domain p={p} |B|={k} observed={}", observed.len());
            if args.require_coverage {
                let expected = all_canonical_b(p, k);
                let missing: Vec<_> = expected.difference(&observed).take(5).cloned().collect();
                let extra: Vec<_> = observed.difference(&expected).take(5).cloned().collect();
                println!(
                    "domain p={p} |B|={k} expected_canonical={} missing={} extra={}",
                    expected.len(),
                    expected.difference(&observed).count(),
                    observed.difference(&expected).count()
                );
                if !missing.is_empty() || !extra.is_empty() || expected.len() != observed.len() {
                    return Err(format!(
                        "coverage failure for p={p} |B|={k}: sample_missing={missing:?} sample_extra={extra:?}"
                    ));
                }
            }
        }
    }

    println!("verified_rows={rows}");
    println!("unique_instances={}", seen.len());
    println!("PASS rust minimal witness verification");
    Ok(())
}
