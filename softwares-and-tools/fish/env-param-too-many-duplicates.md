---
date: 2024-03-18
Fish shell version: 3.7.0
os: macos
---

## Problem

When `echo $PATH`, many paths appears for tens of times. 

## Sol

In `config.fish` or so, don't use:

```
set PATH xxx:$PATH
```

Instead, add quotes:

```
set PATH "xxx:$PATH"
```

