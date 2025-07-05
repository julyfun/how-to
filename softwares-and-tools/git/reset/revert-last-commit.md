---
title: revert-last-commit
date: 2024-07-25 14:47:55
tags: ["softwares-and-tools", "git", "commit", "reset"]
---
ref: https://blog.csdn.net/w958796636/article/details/53611133

```
git reset HEAD^
```

HEAD^的意思是上一个版本，也可以写成HEAD~1

如果你进行了2次commit，想都撤回，可以使用HEAD~2

```
--mixed 

意思是：不删除工作空间改动代码，撤销commit，并且撤销git add . 操作

这个为默认参数,git reset --mixed HEAD^ 和 git reset HEAD^ 效果是一样的。

--soft  

不删除工作空间改动代码，撤销commit，不撤销git add . 

--hard

删除工作空间改动代码，撤销commit，撤销git add . 

注意完成这个操作后，就恢复到了上一次的commit状态
```

## undo 第一个 init commit

ref: https://stackoverflow.com/questions/6632191/how-to-revert-initial-git-commit

```
git update-ref -d HEAD
```

