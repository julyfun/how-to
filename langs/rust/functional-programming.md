## Find in a Vec the smallest f(x).unwrap() where f(x) is not None 

```rs
fn func(x: f64) -> Option<f64> {
    if x > 2.5 {
        Some(x + 100.0)
    } else {
        None
    }
}
fn main() {
    let vec = vec![6.0, 5.0, 4.0, 3.0, 2.0, 1.0];
    let min_odd = vec
        .iter()
        .filter_map(|x| func(*x))
        .min_by(|x, y| x.partial_cmp(&y).unwrap_or(std::cmp::Ordering::Equal));

    println!("{min_odd:?}");
}
```

