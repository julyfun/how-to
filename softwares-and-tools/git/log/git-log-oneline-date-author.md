---
ref: https://stackoverflow.com/questions/1441010/the-shortest-possible-output-from-git-log-containing-author-and-date
date: 2024-03-28 09:29:16
title: "git-log-oneline-date-author"
tags: []
---

```
git log --pretty="%C(Yellow)%h  %C(reset)%ad (%C(Green)%cr%C(reset))%x09 %C(Cyan)%an: %C(reset)%s" --date=short -7
```

- ref: https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs

```
git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
```
