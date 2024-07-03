---
reliability: "[40% (author), 0 / 0 (visitor)]"
date: 2024-07-03
language: "en"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
keywords: []
---

# Setup clangd, cmake just like on unix

## Don't

- **Don't use clangd exe downloaded by clangd extension in vscode.**
- Don't need `tasks.json` like files.

## Steps

- Install msys2 https://www.msys2.org/
- Install C++ toolchain

```
pacman -Syu
pacman -S mingw-w64-x86_64-gcc
pacman -S mingw-w64-x86_64-cmake # use cmake --build ., no need make
pacman -S mingw-w64-x86_64-clang
pacman -S mingw-w64-x86_64-clang-tools-extra # clangd is here
```

- Find your `clangd.exe` in `C:\msys64\mingw64\clangd.exe`
- Put the path in your vscode clangd settings.

Done.

## Test

- 
- Create unix like cmake project
- cd build
- cmake ..
- Reload vscode window and see if it can find headers

