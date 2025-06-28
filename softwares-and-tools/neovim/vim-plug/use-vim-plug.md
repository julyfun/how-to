---
title: "use-vim-plug"
date: 2024-01-15 01:10:05
tags: []
---
https://github.com/junegunn/vim-plug

在 init.vim 中加上

```vim
call plug#begin()
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }
call plug#end()
```

然后在一个 nvim 中运行 :PlugInstall

## 配置文件位置

`$HOME/.local/share/nvim/site/autoload/plug.vim`

