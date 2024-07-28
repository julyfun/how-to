How to do anything.

## News!

https://how-to.fun is now available! This site imports how-to as a submodule, so it will automatically update as `how-to` updates! 

## Utils

```
# show abnormal tracked files
git ls-files | grep -v '\.md$' | grep -v '\.md"$'
# list recent updated files (but ordered by name)
git diff --name-only HEAD~100..HEAD
```

## Contributions are welcomed

Feel free to add new articles in this repo.

If you meet problems on editing or pushing, please open an issue.

## Advantages

- Easy to write new articles and synchronize.
- Git provides article histories.
- Plain text which is easy to search, has very few redundant informaiton.
- File & directories structure, familiar and easy to expand. 

## How to make use of this repo

- Search by browsing files, or IDE search engines, or command line tools like `grep` and `find`.
    - Use [autojump](https://github.com/wting/autojump) to locate directories by recent accessed paths.
    - Use [fzf.fish](https://github.com/PatrickF1/fzf.fish) to find articles smoothly.
    - Alternative: `mfa` fish shell tools. See [mfa.fish](https://github.com/julyfun/mfa.fish).
- Articles may be written in non-english language. Use Google Translate then, most of the time it's useful. 
- Create new articles freely if you think this can help people. Try not to provide confusing information.

## To do

- [x] Better commit message by fish shell script.
- [x] Smart content search engine. `jd` and `jst gf`.
- [ ] Integrate to `mfa.fish`.
- [ ] Website for this repo.
- [ ] Identify language and location of an article.

## Do

- List the links. For respect to the author and reference.

## Don't do

- Spending too much time answering or editing questions that relies largely on proficiency.

## File Suffixes

- `.1.md`: Don't know how, this is a question.
- `.todo.md`: Knowing how, but not written yet.
- `.old.md`: Should be removed cuz too old.

---

### Types of answers

- 使用某种工具过程中，出现了报错 / 意外，如何解决？
    - 例：打开 `neovim` 出现了带有 `E303` 关键字的错误，通常是因为什么？如何解决？
- 遭遇某种需求，知道存在一种工具，如何安装和使用这种工具？是否已存在更先进工具 / 替代工具？
    - 例：需要强制命令行走代理，知道 `proxychains` 工具可能解决此需求，问该工具是否兼容 macos？如何安装和使用，安装和使用中可能会遇到什么问题？
    - 例：在 Ubuntu 中希望更好的终端，知道 `konsole` 工具，问如何安装、配置和使用该工具？

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

