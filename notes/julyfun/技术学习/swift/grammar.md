---
title: grammar
date: 2025-06-12 21:36:58
tags: ["notes", "julyfun", "技术学习", "swift"]
---
- @escaping 闭包
    - 这个闭包要逃逸出其所在函数的时候，即必须用 @escaping
    - 例如放到 DispatchQueue.global().async {} 中时. 
