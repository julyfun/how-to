---
reliability: "[20% (author), 0 / 0 (visitor)]"
language: "zh-hans"
os: "Linux DESKTOP-I44J4US 5.15.153.1-microsoft-standard-WSL2 #1 SMP Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: [computer]
date: 2024-07-01
title: Could not load library dlopen error: /home/julyfun/ros_ws/install/tf_test/lib/libtf_test.so: undefined symbol
tags: []
---

# Could not load library dlopen error: /home/julyfun/ros_ws/install/tf_test/lib/libtf_test.so: undefined symbol

```
terminate called after throwing an instance of 'class_loader::LibraryLoadException'
  what():  Could not load library dlopen error: /home/julyfun/ros_ws/install/tf_test/lib/libtf_test.so: undefined symbol: _ZTVN7tf_test6TfTestE, at ./src/shared_library.c:99
[ros2run]: Aborted
```

maybe you forget to implement the destructor. (guess why it is runtime error)

