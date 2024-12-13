How to do anything.

!!! tip "News"

    [how-to.fun](https://how-to.fun) is now available! This site imports how-to as a submodule, so it will automatically update as `how-to` updates!

!!! warning "Old articles here may be CSDN-like"

    New articles here will provide better problem-related information.

## Search your tricks in:

- NOTE
- time note (24/09, 24/11...)
- by folder and file name (jd)

## To do

- [x] Better commit message by fish shell script.
- [x] Smart content search engine. `jd` and `jst gf`.
- [x] Integrate to `mfa.fish`.
- [x] Website for this repo.
- [ ] Identify language and location of an article.

## Do

- List the links. For respect to the author and reference.

## Don't do

- Spending too much time answering or editing questions that relies largely on proficiency.

---

### Information needed for judging reliability

- 文章语言 (Language)
- 作者和联系方式（用于追问） - 自动生成
- 作者假定读者知道什么知识。（例如：矩阵乘法, 熟练掌握傅里叶分析, brew）
- 信息来源：是第一手找到解决方案，还是在 StackOverflow 等地找到其他人解决方案，并在本人环境验证其可行？
- 如何复现？环境：操作系统以及版本，实践日期，`uname -a`，gcc 等软件版本
- 验证者 testers 和验证次数，包括原作者的使用次数。
- 评论者。
- 作者评估，该文章有多高可信度？

### Which answers are needed

- 网站 SSL 证书过期，如何重新申请并配置新 SSL 证书？这种问题容易忘记，而写一篇文章可以很好规避再次犯错。

### Which answers are not needed

- 课堂笔记类。有些问题极大程度上依靠熟练度解决，本仓库不应该花时间回答这类问题。
- 有对应的具体文档的系统内容。例如 iPadOS 如何关闭检测 Mac 的鼠标和键盘。这些问题有官方的系统的文档，不应该花时间重新写一份，导致抢占官方文档的地位。

## Utils

```
# show abnormal tracked files
git ls-files | grep -v '\.md$' | grep -v '\.md"$'
# list recent updated files (but ordered by name)
git diff --name-only HEAD~100..HEAD
```

```
watch -n 1800 fish -c "jp"
```

- type

```
.h
.md
.rs
.js
.py
.jpg
.typ
.gitignore
.css
.cpp
.json
.png
.ipynb
.txt
.vimrc
```

