---
os: macos
date: 2024-02-19 14:30:11
title: cant-find-std-header-file-like-algorithm
tags: []
---

If header file like this shows an error:

```
#include <algorithm>
```

Then check your clangd output in vscode panel. Clangd could have found a wrong `compile_commands.json`. In fact, clangd always trys to find a `build/compile_commands.json` from parent folder.

## solution

You can copy a `build/compile_commands.json` into current workspace from some other directories.

