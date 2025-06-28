---
title: "download-failed"
date: 2024-01-15 01:10:05
tags: []
---
修改默认下载 url 格式。

https://www.bilibili.com/read/cv21439638/

根据这篇文章：

- 在 `~/.local/share/nvim/site/pack/packer/start/packer.nvim/lua/packer.lua` 中找到 `default_url_format` 字段并由 `https://github.com/%s.git` 改为 `git@github.com:%s`.

