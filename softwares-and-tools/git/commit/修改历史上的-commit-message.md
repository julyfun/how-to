---
reliability: "20% (author)"
os: "Linux Manjusaka 5.15.153.1-microsoft-standard-WSL2 #1 SMP Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: "Manjusaka"
assume-you-know: [computer]
date: 2025-06-01
title: 修改历史上的 commit message
tags: []
---

# 修改历史上的 commit message

- 要修改的 commit hash code 假设为 A
- git rebase -i A~1
- 会出现一个编辑界面，在需要修改的 commit 的 hash 前面把 `pick` 改为 `edit`
- `git commit --amend` 修改 message
- `git rebase --continue`
- `git push -f`
