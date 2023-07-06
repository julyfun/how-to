## 使用系统粘贴板
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

## 在 plugins.lua 中加入新的插件

在 return 的内部而不是外部：

```
  use({ 'rose-pine/neovim', as = 'rose-pine' })
  vim.cmd('colorscheme rose-pine')
```
