---
title: cmake-no-pybind11-config-cmake
date: 2023-09-15 21:11:26
tags: []
---
## Fault

```
CMake Error at CMakeLists.txt:7 (find_package):
  By not providing "Findpybind11.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "pybind11",
  but CMake did not find one.

  Could not find a package configuration file provided by "pybind11" with any
  of the following names:

    pybind11Config.cmake
    pybind11-config.cmake

  Add the installation prefix of "pybind11" to CMAKE_PREFIX_PATH or set
  "pybind11_DIR" to a directory containing one of the above files.  If
  "pybind11" provides a separate development package or SDK, be sure it has
  been installed.
```

## Sol

激活一个有 pybind 的 conda 环境。

例如

```
conda activate cloth-funnels
```

