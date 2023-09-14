## 使用系统粘贴板

in init.vim:

set clipboard=unnamedplus

## `~/.config/nvim`

nvim
├── init.vim
└── lua
    └── plugins.lua

- 注意在 init.vim 中加入 lua 语句：

```
lua require('plugins')
```

- 其中的 plugins.lua 来自

```
https://github.com/wbthomason/packer.nvim
```

## 在 Packer plugins.lua 中加入新的插件

在 return 的内部而不是外部：

```
  use({ 'rose-pine/neovim', as = 'rose-pine' })
  vim.cmd('colorscheme rose-pine')
```


## fish 没有高亮

nvim 版本太低

## 如果装了 Packer 以后一进 nvim 就报错

```
Error detected while processing /home/strife/.local/share/nvim/plugged/nvim-treesitter/plugin/nvim-treesitter.lua:
E5113: Error while calling lua chunk: .../plugged/nvim-treesitter/lua/nvim-treesitter/configs.lua:104: attempt to call field 'nvim_create_augroup' (a
nil value)
```

这是因为 nvim 版本太低

## 再装一个 vim-plug

https://github.com/junegunn/vim-plug


## 然后再装一个多光标

https://github.com/mg979/vim-visual-multi

