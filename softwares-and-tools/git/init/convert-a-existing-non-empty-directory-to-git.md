---
title: convert-a-existing-non-empty-directory-to-git
date: 2024-03-28 09:29:16
tags: []
---
According to:

https://stackoverflow.com/questions/3311774/how-to-convert-existing-non-empty-directory-into-a-git-working-directory-and-pus

非空文件夹是可以 git init 的。

you need:

```
cd <localdir>
git init
git add .
git commit -m 'message'
git remote add origin <url>
git push -u origin main
```

