```
os: macos
```

- 查看所有字体及其变体

```
typst fonts --variants | nvim
```

注意，很多字体安装时带有各种变体，但是 `typst` 似乎无法找到这些变体。你可以下载本体就是变体的字体，比如直接谷歌搜索下载思源宋体的粗体版本，这样就可以使用了。

然后在文章开头这样指定字体：

```typst
#set text(
  font: ("New Computer Modern", "Source Han Serif SC")
)
```

