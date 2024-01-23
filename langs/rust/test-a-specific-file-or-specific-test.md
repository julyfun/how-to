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

