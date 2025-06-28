---
title: restore-cur-dir
date: 2024-04-03 13:35:14
tags: []
---
ref: https://stackoverflow.com/questions/15404535/how-to-git-reset-hard-a-subdirectory

```
git restore --source=HEAD --staged --worktree -- .
git restore -s@ -SW -- <path>
```

