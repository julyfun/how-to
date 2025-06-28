---
author: julyfun
reliability: 20%
---
****
## 1. 常规读入输出

我们常规读入和输出用的是 `input()` 和 `print()`:

```py
n = int(input())
li = list(map(int, input().split())) # 读入一行数，存储到列表
print('Hello world')
print(li[0])
```

## 2. 格式化字符串

用 `f` 作为前缀的字符串可以将其中花括号中的内容自动转换：

```py
n = 123
m = 1234
s = f'{n} + {m} = {n + m}'
# 现在 s 就是 '123 + 1234 = 1357' 了，太神奇了
```

这种字符串叫做格式化字符串。

## 3. 文件输入输出

USACO 比赛中用不上，但是平时可能有用。

```py
# 这里新建了一个变量 fin，后面 open 表示打开文件，'1.in' 是文件名，'r' 表示要读入
# 必须保证 1.in 与 python 源文件在同一个文件夹下哦
fin = open('1.in', 'r')
# 'w' 表示要输出
fout = open('1.txt', 'w')

# 接下来就是把 input() 换成 fin.readline()，从文件中读入
n = int(fin.readline())
li = list(map(int, fin.readline().split()))
# 如果要输出到文件，那么可以用格式化字符串 
fout.write('Hello world\n')
fout.write(f'{li[0]}\n')
```

## 4. 如何用 USACO test data 自行评测

打开形如这样的地址下载题目的 test data，你可以把下面这行的 `jan22` 改成 `dec21` 之类的来切换比赛：

http://www.usaco.org/index.php?page=jan22results

![](/assets/WechatIMG6.png)

下载完以后解压得到 `1.in` `1.out` `2.in` `2.out` 等文件。

其中 `1.in` `1.out` 表示第一个测试点的输入数据和标准答案。你可以在运行 python 的时候复制粘贴，也可以用文件读入输出。

```py
fout = open('1.txt', 'w')
# ... 下面输出到 1.txt 中
```

输出到 `1.txt` 后，你可以在终端使用 `diff` 命令比较两个文件。

```
diff 1.txt 1.out
```

如果你的答案和标准答案一样，那么 `diff` 命令不会有任何输出。如果不一样，他就会告诉你哪里不一样，例如：

```
$ diff 2.out 2.txt
1c1
< hello world: 58
---
> hello world: 59
\ No newline at end of file
```

