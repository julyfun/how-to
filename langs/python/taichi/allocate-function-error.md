---
os: ubuntu
date: 2024-02-01
title: allocate-function-error
tags: ["langs", "python", "taichi"]
---
```
/home/julyfun/code/taichi-mpm/taichi/external/include/spdlog/fmt/bundled/format.h: In instantiation of ‘void fmt::internal::MemoryBuffer<T, SIZE, Allocator>::grow(std::size_t) [with T = char; long unsigned int SIZE = 500; Allocator = std::allocator<char>; std::size_t = long unsigned int]’:
/home/julyfun/code/taichi-mpm/taichi/external/include/spdlog/fmt/bundled/format.h:797:6:   required from here
/home/julyfun/code/taichi-mpm/taichi/external/include/spdlog/fmt/bundled/format.h:801:30: error: no matching function for call to ‘fmt::internal::MemoryBuffer<char, 500, std::allocator<char> >::allocate(std::size_t&, std::nullptr_t)’
  801 |   T *new_ptr = this->allocate(new_capacity, FMT_NULL);
      |                ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
```

可能你在使用错误环境下的 taichi。检查 .bashrc 之类的配置文件中是否指定了 TAICHI_REPO_DIR 等环境变量，如果指定了，删掉试试，2024-2-1 以此解决。

