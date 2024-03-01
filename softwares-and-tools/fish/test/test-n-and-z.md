---
fish shell version: 3.7.0
---

## Strange `-n`

```fish
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

