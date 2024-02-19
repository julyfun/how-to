---
os: macos
---

If header file like this shows an error:

```
#include <algorithm>
```

Then check your clangd output in vscode panel. Clangd could have found a wrong `compile_commands.json`. In fact, clangd always trys to find a `build/compile_commands.json` from parent folder.

## solution

You can copy a `build/compile_commands.json` into current workspace from some other directories.

