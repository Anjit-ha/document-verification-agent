use pyo3::prelude::*;
use std::collections::{HashSet, hash_map::DefaultHasher};
use std::hash::{Hash, Hasher};


// -----------------------------------------------------
// Normalize Text
// -----------------------------------------------------

#[pyfunction]
fn normalize_text(text: &str) -> String {

    text
        .to_lowercase()
        .replace(",", "")
        .replace(".", "")
        .replace("\n", " ")
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")

}


// -----------------------------------------------------
// Fast Hash
// -----------------------------------------------------

#[pyfunction]
fn hash_text(text: &str) -> u64 {

    let mut hasher = DefaultHasher::new();

    text.hash(&mut hasher);

    hasher.finish()

}


// -----------------------------------------------------
// Jaccard Similarity
// -----------------------------------------------------

#[pyfunction]
fn jaccard_similarity(a: &str, b: &str) -> f64 {

    let set_a: HashSet<&str> = a.split_whitespace().collect();

    let set_b: HashSet<&str> = b.split_whitespace().collect();

    let intersection =
        set_a.intersection(&set_b).count() as f64;

    let union =
        set_a.union(&set_b).count() as f64;

    if union == 0.0 {

        return 0.0;

    }

    intersection / union

}


// -----------------------------------------------------
// Exact Match
// -----------------------------------------------------

#[pyfunction]
fn exact_match(a: &str, b: &str) -> bool {

    normalize_text(a) == normalize_text(b)

}


// -----------------------------------------------------
// Contains Match
// -----------------------------------------------------

#[pyfunction]
fn contains_match(a: &str, b: &str) -> bool {

    let aa = normalize_text(a);

    let bb = normalize_text(b);

    aa.contains(&bb) || bb.contains(&aa)

}


// -----------------------------------------------------
// Word Count
// -----------------------------------------------------

#[pyfunction]
fn word_count(text: &str) -> usize {

    text.split_whitespace().count()

}


// -----------------------------------------------------
// Remove Duplicate Lines
// -----------------------------------------------------

#[pyfunction]
fn unique_lines(text: &str) -> Vec<String> {

    let mut seen = HashSet::new();

    let mut result = Vec::new();

    for line in text.lines() {

        let line = line.trim();

        if !line.is_empty() && seen.insert(line.to_string()) {

            result.push(line.to_string());

        }

    }

    result

}


// -----------------------------------------------------
// Rust Module
// -----------------------------------------------------

#[pymodule]
fn rust_utils(
    _py: Python,
    m: &Bound<'_, PyModule>
) -> PyResult<()> {

    m.add_function(
        wrap_pyfunction!(normalize_text, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(hash_text, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(jaccard_similarity, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(exact_match, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(contains_match, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(word_count, m)?
    )?;

    m.add_function(
        wrap_pyfunction!(unique_lines, m)?
    )?;

    Ok(())
}