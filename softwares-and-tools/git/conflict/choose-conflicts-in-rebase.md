---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-06-02
language: Chinese
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: Julyfun MacOS14.5 M1
suppose-you-know: computer
keywords:
---

# choose Conflicts in rebase

![image.png|800](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250520003409.png)

情况：origin/main 上别人有新 push，本地 main 上自己有 commit，pull with rebase 时发生冲突
打开 vscode 合并冲突界面，左边是 origin/main，右边是本地的新 commit

> 测试完了，确实是这样。