---
title: quick-line-jumps
date: 2024-01-15 01:10:05
tags: []
---
https://github.com/Houl/repmo-vim/tree/master

put this autoload in your nvim autoload

and paste stuffs like

```vim
" map a motion and its reverse motion:
:noremap <expr> h repmo#SelfKey('h', 'l')|sunmap h
:noremap <expr> l repmo#SelfKey('l', 'h')|sunmap l

" if you like `:noremap j gj', you can keep that:
:map <expr> j repmo#Key('gj', 'gk')|sunmap j
:map <expr> k repmo#Key('gk', 'gj')|sunmap k

" repeat the last [count]motion or the last zap-key:
:map <expr> ; repmo#LastKey(';')|sunmap ;
:map <expr> , repmo#LastRevKey(',')|sunmap ,

" add these mappings when repeating with `;' or `,':
:noremap <expr> f repmo#ZapKey('f')|sunmap f
:noremap <expr> F repmo#ZapKey('F')|sunmap F
:noremap <expr> t repmo#ZapKey('t')|sunmap t
:noremap <expr> T repmo#ZapKey('T')|sunmap T

" 只记忆 count jumps
:let g:repmo_require_count = 1
```

in your init.vim.

## Usage

5j;;;;hjkl;;;

It will remember 5j, not one of hjkl.

just kidding, although https://www.vim.org/scripts/script.php?script_id=2174 says so, it doesn't seem to work now.

