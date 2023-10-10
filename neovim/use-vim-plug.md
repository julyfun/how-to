https://github.com/junegunn/vim-plug

在 init.vim 中加上

```vim
call plug#begin()
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }
call plug#end()
```

然后在一个 nvim 中运行 :PlugInstall

