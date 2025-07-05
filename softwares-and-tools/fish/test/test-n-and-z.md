---
fish-shell-version: 3.7.0
date: 2024-03-01 21:19:42
title: ttt is not set
tags: ["softwares-and-tools", "fish", "test"]
---
## TLDR

`test -n` returns true iff string is unset or (set and non-zero); (in fact because -n didn't receive any string)

`test -z` return true iff string is unset or (set and zero);

## Strange `-n`

```fish
# ttt is not set
if test -n $ttt
    echo 1
else
    echo 0
end
```

This outputs 1. (**Strange**)

```fish
set ttt ""
if test -n $ttt
    echo 1
else
    echo 0
end
```

This outputs 0.

## Command `-z`

```fish
if test -z $ttt
    echo 1
else
    echo 0
end
```

This outputs 1.

```fish
set ttt ""
if test -z $ttt
    echo 1
else
    echo 0
end
```

This still outputs 1. Consistent.

