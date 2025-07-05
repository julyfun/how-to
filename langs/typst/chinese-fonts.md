---
os: macos
date: 2024-04-01
title: chinese-fonts
tags: ["langs", "typst"]
---
- 查看所有字体及其变体

```
typst fonts --variants | nvim
```

注意，很多字体安装时带有各种变体，但是 `typst` 似乎无法找到这些变体。你可以下载本体就是变体的字体，比如直接谷歌搜索下载思源宋体的粗体版本，这样就可以使用了。但是这样也有问题：所有中文字体都将会是粗体。

因此，你可以使用 "Songti SC" 等自带 Weight 而不是变体的字体。

ref: https://github.com/typst/typst/issues/185

> Typst does not support variable fonts at the moment.

- 指定字体

在文章开头这样指定字体：

```typst
#set text(
  font: ("New Computer Modern", "Source Han Serif SC")
)
```

