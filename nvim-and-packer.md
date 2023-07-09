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

## 在 plugins.lua 中加入新的插件

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

## 先贴一些宝贝在

```vim
" Configuration file for vim
set modelines=0		" CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility
" remove change the following statements
set nocompatible	" Use Vim defaults instead of 100% vi compatibility
set backspace=2		" more powerful backspacing

" Don't write backup file if vim is being called by "crontab -e"
au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
au BufWrite /private/etc/pw.* set nowritebackup nobackup

" 自定义设置
" set mouse=a

let skip_defaults_vim=1

syntax enable                " 打开语法高亮
syntax on                    " 开启文件类型侦测

colorscheme desert           " 着色模式:灰色背景
set guifont=Monaco:h14

set autoindent               " 自动对齐
set backspace=2              " 设置退格键可用
set cindent shiftwidth=4     " 自动缩进4空格
set smartindent              " 智能自动缩进
set ai!                      " 设置自动缩进
set nu!                      " 显示行号
set showmatch                " 显示括号配对情况
" set mouse=a                  " 启用鼠标
set ruler                    " 右下角显示光标位置的状态行
set incsearch                " 查找book时，当输入/b时会自动找到
set hlsearch                 " 开启高亮显示结果
set incsearch                " 开启实时搜索功能
set nowrapscan               " 搜索到文件两端时不重新搜索
set nocompatible             " 关闭兼容模式
set cursorline               " 突出显示当前行
set hidden                   " 允许在有未保存的修改时切换缓冲区
set list                     " 显示Tab符，使用一高亮竖线代替
set listchars=tab:\|\        " 显示Tab符，使用一高亮竖线代替
set noswapfile               " 设置无交换区文件"
set writebackup              " 设置无备份文件
set nobackup                 " 设置无备份文件
set autochdir                " 设定文件浏览器目录为当前目录
set foldmethod=syntax        " 选择代码折叠类型
set foldlevel=100            " 禁止自动折叠
set laststatus=2             " 开启状态栏信息
set cmdheight=2              " 命令行的高度，默认为1，这里设为2
set showtabline=2            " 设置默认显示标签
set clipboard+=unnamed       " 与系统公用剪贴板
set autoread                 " 当文件在外部被修改，自动更新该文件
set scrolloff=5              " 设定光标离窗口上下边界 5 行时窗口自动滚动
set guioptions-=T            " 去掉上方工具栏
set autochdir                " 自动切换到当前目录"
set autoread                 " 自动检测并加载外部对文件的修改"
set autowrite                " 自动检测并加载外部对文件的修改"
set showcmd                  " 命令栏显示命令 "
set ignorecase smartcase     " 搜索时智能忽略大小写
set tabstop=4 " (ts) 设置一个 <tab> 显示为多少个空格
set expandtab " (et) 把 <tab> 转换为空格
set shiftwidth=4 " (sw) 设置自动缩进的宽度（以及 << 和 >> 命令）
set number
set relativenumber

" [总是使用系统粘贴板]
set clipboard=unnamedplus

" [删除而不是剪切]
nnoremap d "_d
vnoremap d "_d
nnoremap D "_D
vnoremap D "_D
nnoremap c "_c
vnoremap c "_c
nnoremap C "_C
vnoremap C "_C
xnoremap p pgvy

" [括号补全]
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i

" [vim-plug]
call plug#begin()
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
call plug#end()

" [添加 Packer]
lua require('plugins')
```
