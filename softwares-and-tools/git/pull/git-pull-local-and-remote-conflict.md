---
title: git-pull-local-and-remote-conflict
date: 2024-03-28 09:29:16
tags: ["softwares-and-tools", "git", "pull"]
---
Commits like

```
local:  xxx -> some commit
remote: xxx -> yyy -> zzz
```

Now, `git pull` locally is not valid.

What to do?

## Well you should git rebase, it rebases automatically

