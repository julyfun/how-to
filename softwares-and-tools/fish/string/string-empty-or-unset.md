---
title: string-empty-or-unset
date: 2024-01-16 21:21:18
tags: ["softwares-and-tools", "fish", "string"]
---
https://stackoverflow.com/questions/47743015/fish-shell-how-to-check-if-a-variable-is-set-empty

unset 就是 empty. 但是 string length empty 不会输出，string length "" 输出 0

test -n "$var": var set and its length >= 1

test -z "$var": var set and its length == 0

但是 test -z 可以不接收参数，test -n 不接收居然会返回 true.

