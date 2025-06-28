---
title: E303-Unable-to-open-swap-file
date: 2024-01-22 22:11:17
tags: []
---
## 1

May be because you previously loaded a vim script initialization file, but you failed to load that file now.

## 2

Check if your `~/.config/nvim/init.vim` exists.

- Once Julyfun renamed `init.vim` to `init.nvim` and E303 occurs.

## 3

- ref: https://www.markhneedham.com/blog/2024/01/03/nvim-swap-file-permission-denied/

- ref: https://github.com/neovim/neovim/issues/3898

Check the owner of ~/.local/share/nvim/swap

Do something like:

```
sudo chown <user_name>:<group_name>  swap
```

