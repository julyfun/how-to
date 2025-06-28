---
title: "delete-all-previously-tracked-but-should-be-ignored-files"
date: 2024-01-22 18:49:31
tags: []
---
https://stackoverflow.com/questions/1274057/how-do-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore?page=1&tab=scoredesc#tab-top

no better way but:

```
git rm -r --cached .
git add .
```

