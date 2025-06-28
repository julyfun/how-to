---
title: when-remote-branch-renamed
date: 2023-11-20 18:26:41
tags: []
---
```
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

