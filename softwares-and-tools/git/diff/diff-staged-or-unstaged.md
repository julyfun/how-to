---
title: "diff-staged-or-unstaged"
date: 2024-03-30 17:40:32
tags: []
---
ref: https://stackoverflow.com/questions/1587846/how-do-i-show-the-changes-which-have-been-staged

```
git diff # show unstaged but tracked
git diff --cached # show staged
git diff HEAD # show staged and unstaged (till last commit)

git diff --name-only --cached # show file names only
```

