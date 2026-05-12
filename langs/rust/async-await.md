---
title: async-await
date: 2024-01-15 01:10:05
tags: ["langs", "rust"]
---

古早疑问：

> 异步，多线程和并行的区别？ - 知则的回答 - 知乎
>
> https://www.zhihu.com/question/28550867/answer/2207913049
>
> async 函数可以在自己被阻塞时，中断自己的执行并把 CPU 控制权交还给调用自己的函数。
>
> 那么 async 函数如何被判定为阻塞呢？单线程的 async 函数在什么条件下会交还控制权呢？

26/5/13 upd:
1. tokio::spawn() : 其他线程 fire and forget （根据视频，不是其他线程池）
2. func().await : 同线程阻塞并等待结果
3. tokio::join! : 同线程并发并等待所有结果
4. tokio::select! : 同线程并发并等待最早结果，唯一会自动 cancel future 的，需要保证 cancellation safety
5. tokio::spawn_blocking(move || func()).await : 其他线程池 fire 并等待结果，当前线程可 yield

ref: https://www.bilibili.com/video/BV17Z5w6GEbG/?spm_id_from=333.1387.favlist.content.click&vd_source=e91cd5187b413becc0ce8b3bb56435c9
