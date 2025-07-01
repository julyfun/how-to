---
title: async-await
date: 2024-01-15 01:10:05
tags: ["langs", "rust"]
---
异步，多线程和并行的区别？ - 知则的回答 - 知乎

https://www.zhihu.com/question/28550867/answer/2207913049

async 函数可以在自己被阻塞时，中断自己的执行并把 CPU 控制权交还给调用自己的函数。

那么 async 函数如何被判定为阻塞呢？单线程的 async 函数在什么条件下会交还控制权呢？

