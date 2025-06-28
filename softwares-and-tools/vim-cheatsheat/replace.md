---
title: "replace"
date: 2024-01-15 01:10:05
tags: []
---
https://www.baeldung.com/linux/vim-search-replace#:~:text=The%20simplest%20way%20to%20perform,the%20dot%20to%20replace%20it.&text=This%20will%20highlight%20the%20first,key%20to%20jump%20to%20it.

## cgn 方法

就是说在下一个单词处执行上一个命令。首先：

```
/word
```

回车跳到一个单词上，然后

```
cgn
```

之后用 `n.` 进行快捷修改。

## another method

```
:%s/aaa/bbb/g
```

