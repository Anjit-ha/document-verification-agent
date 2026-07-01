use pyo3::prelude::*;
use std::collections::HashSet;

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

#[pyfunction]
fn hash_text(text: &str) -> u64 {
    use std::collections::hash_map::DefaultHasher;
    use std::hash::{Hash, Hasher};

    let mut hasher = DefaultHasher::new();
    text.hash(&mut hasher);
    hasher.finish()
}

#[pyfunction]
fn jaccard_similarity(a: &str, b: &str) -> f64 {
    let set_a: HashSet<&str> = a.split_whitespace().collect();
    let set_b: HashSet<&str> = b.split_whitespace().collect();

    let intersection = set_a.intersection(&set_b).count() as f64;
    let union = set_a.union(&set_b).count() as f64;

    if union == 0.0 {
        return 0.0;
    }

    intersection / union
}

#[pymodule]
fn rust_utils(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(normalize_text, m)?)?;
    m.add_function(wrap_pyfunction!(hash_text, m)?)?;
    m.add_function(wrap_pyfunction!(jaccard_similarity, m)?)?;
    Ok(())
}