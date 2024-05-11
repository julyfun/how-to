---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-05-11
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
keywords: []
---

# How to list symbolic link chains?

ref: https://serverfault.com/questions/115856/how-to-list-symbolic-link-chains

```
$ namei d
f: d
 l d -> c
   l c -> b
     l b -> a
       d a
```

