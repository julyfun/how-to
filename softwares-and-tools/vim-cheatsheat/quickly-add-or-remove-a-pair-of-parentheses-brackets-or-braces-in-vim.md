---
title: quickly-add-or-remove-a-pair-of-parentheses-brackets-or-braces-in-vim
date: 2024-01-15 01:10:05
tags: []
---
https://stackoverflow.com/questions/2084210/how-to-quickly-remove-a-pair-of-parentheses-brackets-or-braces-in-vim

you need `'tpope/vim-surround'`

- remove: `ds(`
- add: `ysiw(`

```
ys$` select util end of line and add `
```

