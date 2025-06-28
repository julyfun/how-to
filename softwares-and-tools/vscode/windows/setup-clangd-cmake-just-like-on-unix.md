---
reliability: "[40% (author), 0 / 0 (visitor)]"
language: "en"
os: "win10"
author: "Julyfun MacOS14.5 M1"
suppose-you-know: [computer]
date: 2024-07-03
title: "Setup clangd, cmake just like on unix"
---

# Setup clangd, cmake just like on unix

ref: https://blog.csdn.net/tyKuGengty/article/details/120119820 (not reliable)
ref: https://www.perplexity.ai/search/windows-shang-ru-he-huo-qu-he-UAy020tWRWG50tRSmDYuIw#0

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

- Create unix like cmake project
- cd build
- cmake ..
- Reload vscode window and see if it can find headers

## If you want lsp without cmake

Add this two flags to your vscode clangd fallback flags:

```
-IC:/msys64/mingw64/include/c++/14.1.0
--target=x86_64-w64-windows-gnu
```

check if a single file can find headers.

(Tested ok)

## Use ninja

In msys2:

```
pacman -S mingw-w64-x86_64-ninja
```

Write cmake as usual. ref: https://blog.51cto.com/u_15127539/3336648

```
cd build
# I forget if I need to specify "build for ninja". This just works on my win10 now
cmake ..
ninja install
```

Go to `install/bin/` and check generated executable.

