---
title: "string-regex-get-variable"
date: 2024-01-16 21:21:18
tags: []
---
```
    git remote -v | string match -rq 'github\.com:(?<remote>[\S]+)\.git'
```

(?<name>...) 其中 ... 是要变量的 regex，而匹配的结果会存储到 $name 这个变量中。

