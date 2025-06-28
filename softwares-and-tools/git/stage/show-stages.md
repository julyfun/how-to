---
title: "show-stages"
date: 2024-03-28 09:25:09
tags: []
---
ref: https://stackoverflow.com/questions/1587846/how-do-i-show-the-changes-which-have-been-staged

```
git diff # show unstaged
git diff --cached # show staged
git diff HEAD # show staged and unstaged (till last commit)

git diff --name-only --cached # show file names only
```

