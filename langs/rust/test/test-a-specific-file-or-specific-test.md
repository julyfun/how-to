---
title: To show output
date: 2024-04-28 10:35:52
tags: []
---
ref: https://stackoverflow.com/questions/54585804/how-to-run-a-specific-unit-test-in-rust

```
rustc --test <file>
```

This generates a binary file. Then if you run the binary file, all tests will be conducted. Source code format be like:

```
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tuple_out_of_range_positive() {
        assert_eq!(
            Color::try_from((256, 1000, 10000)),
            Err(IntoColorError::IntConversion)
        );
    }
```

To run a specific test, run: 

```
./xxx --exact test::test_tuple_out_of_range_positive
```

## Cargo way

```
cargo test test_fn_name # filters with test_fn_name
cargo test test_fn_name -- --exact
cargo test test_mod_name::test_fn_name -- --exact
cargo test --package school_info repeat_students_should_not_get_full_marks -- --exact
# To show output
cargo test --package py-like --test io -- tests::main --exact --nocapture
# test1() in helper.rs
cargo test helper::test1 -- --exact
```

