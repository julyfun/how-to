---
title: jpeg-to-uint8-mat
date: 2024-01-15 01:10:05
tags: []
---
* Step 0: Resize:

https://www.simpleimageresizer.com/resize/jpg

* Step 1: This would turn jpeg to ppm-p6.

https://onlineconvertfree.com/zh/convert-format/jpg-to-ppm/

* step2: This turns ppm-p6 to ppm-p3:

https://thomasebsmith.github.io/ppm-converter/

* step3: use `ppm_load()` function in this file:

https://github.com/julyfun/find-light-circle/blob/28de4d34d8a8063486688e5545778720e6fb9798/main.c

