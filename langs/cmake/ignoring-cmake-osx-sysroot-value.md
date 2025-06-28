---
title: Ignoring CMAKE_OSX_SYSROOT value
date: 2024-07-31 16:35:06
tags: []
---
# Ignoring CMAKE_OSX_SYSROOT value

??? info "Problem environment"

    - author: Julyfun MacOS14.5 M1
    - edited date: 2024-07-31
    - expected environment: Darwin 192.168.124.13 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64

## Details of the problem / Steps to reproduce the error

cli cmake an old project warns:

```
CMake Warning at /opt/homebrew/Cellar/cmake/3.29.2/share/cmake/Modules/Platform/Darwin-Initialize.cmake:308 (message):
  Ignoring CMAKE_OSX_SYSROOT value:

   /Library/Developer/CommandLineTools/SDKs/MacOSX14.0.sdk

  because the directory does not exist.
Call Stack (most recent call first):
  /opt/homebrew/Cellar/cmake/3.29.2/share/cmake/Modules/CMakeSystemSpecificInitialize.cmake:34 (include)
  CMakeLists.txt:2 (project)
```

and build failed.

---

## Answer 1

??? info "Answer environment"

    - author: As in the problem
    - edited date: As in the problem
    - verified environment: As in the problem
    - assume readers know: _No assumption_

- ref: https://stackoverflow.com/questions/32720564/cmake-broken-after-update-to-xcode-7-0

`rm -r *` in your build cache folder. Done.

