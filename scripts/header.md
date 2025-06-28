---
title: header
date: 2025-06-28 17:31:39
tags: []
---
写一个 python 脚本，对输入文件夹下所有的 .md 文件 (recursively)

如果文章第一行开头是
"- <小写字母>"，则文件类型为 A. 如果文章第一行是 "---"，且后面还有 "---" 的一行，则文件类型为 B. 否则文章类型为 C.
对于每个文章，检测首个以 "# " 开头的行。记 "# " 后的内容为 rec_title（如果没有 "# " 则 sharp_title 为文件名，不含 .md）

定义函数 header，输入一个 string.
assert 其为 B 类型文件。
return 提取第一个 "---" 行和第二个 "---" 行中间的内容

定义函数 recover:
输入一个文章 string
assert 其为 B 类型文件。
提取 header
如果这些行中没有 "title: " 开头的，则添加 "title: " 为rec_title
如果这些行中有 "keywords: " 开头，改为 "tags: " 开头
- 如果没有 tags 和 keywords，添加 "tags: []"
如果这些行中没有 "date: " 开头，添加 "date: " 这个文件的 git 首次 track 时间 (yyyy-mm-ss hh:mm:ss)
返回处理好的内容

## 若文章类型为 A:
提取文件开头连续的每行满足 "- " 开头的行
对于这些行，前后分别加上 "---" "---\n"
并对每行删除开头的 "- "，保留后面的内容
然后 recover

## 若文章类型 B:
recover

## 若文章类型 C:
在文章开头加上
"""
---
title: <rec_title>
date: <git first track date>
tags: []
---
"""

最终要输出到文件里.
