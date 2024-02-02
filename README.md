How to do anything.

## Advantages

- Easy to write new articles and and synchronize.
- Git provides article histories.
- Plain text which is easy to search, has very few redundant informaiton.
- File & directories structure, familiar and easy to expand. 

## How to make use of this repo

- Search via browsing files, or IDE search engines, or command line tools like `grep` and `find`.
    - Or `mfa` fish shell tools. See [https://github.com/julyfun/mfa.fish](https://github.com/julyfun/mfa.fish).
    - `jd <file_or_directory_name>` to locate(`cd`) directories(which are topics), or edit(`nvim`) articles by their names.
    - `jst gf <file_content_or_title>` to search by title and content.
    - `jst find <directory_name_or_file_title>` to search by title.
    - `jst git o <file_path>` to browse the file on github.
    - `jpf <file_path>` to commit and push quickly.
    - Use [autojump](https://github.com/wting/autojump) to locate directories by recent accessed paths.
- Create new articles freely if you think this can help people. Try not to provide confusing information.

## To do

- [x] Better commit message by fish shell script.
- [x] Smart content search engine. `jd` and `jst gf`.
- [ ] Integrate to `mfa.fish`.
- [ ] Website for this repo.

## Do

- List the links. For respect to the author and reference.

## Don't do

---

### Answer types

- 使用某种工具过程中，出现了报错 / 意外，如何解决？
    - 例：打开 `neovim` 出现了带有 `E303` 关键字的错误，通常是因为什么？如何解决？
- 遭遇某种需求，知道存在一种工具，如何安装和使用这种工具？是否已存在更先进工具 / 替代工具？
    - 例：需要强制命令行走代理，知道 `proxychains` 工具可能解决此需求，问该工具是否兼容 macos？如何安装和使用，安装和使用中可能会遇到什么问题？
    - 例：在 Ubuntu 中希望更好的终端，知道 `konsole` 工具，问如何安装、配置和使用该工具？

### Information needed for judging reliability

- 作者和联系方式（用于追问） - 自动生成
- 作者假定读者知道什么知识。（例如：矩阵乘法、熟练掌握傅里叶分析）
- 信息来源：是第一手找到解决方案，还是在 StackOverflow 等地找到其他人解决方案，并在本人环境验证其可行？
- 如何复现？环境：操作系统以及版本，实践日期，`uname -a`，gcc 等软件版本
- 验证者 testers 和验证次数，包括原作者的使用次数。
- 评论者。
- 作者评估，该文章有多高可信度？

