---
title: "print-type"
date: 2024-01-15 01:10:05
tags: []
---
```rs
fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
```

