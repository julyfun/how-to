https://fishshell.com/docs/current/cmds/string-sub.html

```fish
> string sub --length 2 abcde
ab

> string sub -s 2 -l 2 abcde
bc

> string sub --start=-2 abcde
de

> string sub --end=3 abcde
abc

> string sub -e -1 abcde
abcd

> string sub -s 2 -e -1 abcde
bcd

> string sub -s -3 -e -2 abcde
c
```

