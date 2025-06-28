---
title: ROADMAP
date: 2024-07-30 20:30:20
tags: []
---
## Meta

test

回忆提纲需要什么：
- 该名词是做什么的
- 方法是什么，需要什么（接口）

## 非常重要

- [ ] 尽快学习语言
- [ ] yyu 的 rl 教程 https://hrl.boyuai.com/
    - [x] https://hrl.boyuai.com/chapter/1/%E5%A4%9A%E8%87%82%E8%80%81%E8%99%8E%E6%9C%BA
- [ ] d2l 中，搭建优秀网络结构
    - [x] 7.4 Done
    - [x] 7.7 Done
    - [ ] 看下 Googlenet 训练时间和显存占用
  	- [ ] https://d2l.ai/chapter_attention-mechanisms-and-transformers/queries-keys-values.html
- [ ] 上层模型训练 https://blog.csdn.net/qq_42589613/article/details/139207148
  	- [ ] 部署
  	- [ ] 加速

## 有用

  - [ ] Notion 三件套 #private https://www.notion.so/tt-tang/30b7b6709a9641f5bf77b16ca103855c
      - [ ] OPENAI RL https://spinningup.openai.com/en/latest/user/introduction.html
      - [ ] 知乎 https://www.zhihu.com/column/c_1186982555915599872
      - [ ] 实际 research 代码框架 https://github.com/DLR-RM/stable-baselines3
- [ ] mkdocs 网页渲染 typst
- [ ] 编译原理 [[北大编译实践]]
    - [x] https://pku-minic.github.io/online-doc/#/lv1-main/structure
    - [x] https://pku-minic.github.io/online-doc/#/lv1-main/lexer-parser
    - [ ] https://pku-minic.github.io/online-doc/#/lv1-main/parsing-main
- [ ] zig 语法 https://www.zhihu.com/question/50121841/answer/2725592129
- [ ] fishbot 与电机控制
- [ ] 类型体操 pk
    - [ ] day1 https://www.skyzh.dev/blog/2022-01-22-rust-type-exercise-in-database-executors/
    - [ ] 向量化执行引擎： https://blog.csdn.net/qq_35423190/article/details/123129172
    - [ ] comptime: https://blog.zhuangty.com/zig-lang-comptime/
- [ ] 自建通用优化库。先学习 yolo 等，以考虑自变量是否可以是非固定空间。

[[cs自学指南]]

## 一般
- [ ] next.js 创建动态内容 https://segmentfault.com/a/1190000009604779

## TOWRITE

- 电能相比热能的优势
- 解释与预测

![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241120222327.webp)
![image.png](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to/20241120232003.webp)

### 项目概述

在这个项目中，你将实现一个自编码器，用于探索和生成通过组合不同类别的特征向量而生成的混合图像。本项目主要集中在使用**Fashion MNIST**数据集，并且作为一个挑战，你将把相同的方法应用于**CIFAR-100**数据集。

### 任务详情：
1. **数据集准备和过滤**：
    - 加载并预处理Fashion MNIST数据集，确保数据被标准化并分割为训练集和测试集。
    - 过滤数据集以专注于特定类别（例如，运动鞋和T恤）。
2. **自编码器实现**：
    - 设计并实现一个自编码器模型，包括编码器和解码器部分。编码器将输入图像压缩到低维特征空间，解码器则将特征向量还原为图像。
3. **训练自编码器**：
    - 使用训练集数据训练自编码器模型，确保模型能够有效地重建输入图像。
4. **计算类别特征质心**：
    - 计算每个类别的特征质心（即每个类别在特征空间中的平均特征向量）。
5. **生成平均图像**：
    - 使用类别特征质心通过解码器生成每个类别的平均图像。
6. **生成混合图像**：
    - 通过组合不同类别的特征向量生成混合图像，例如，组合运动鞋和T恤的特征向量生成混合图像。
7. **CIFAR-100挑战练习**：
    - 将上述方法应用于CIFAR-100数据集，生成不同类别（例如，汽车和飞机）的混合图像。
### 最终目标
创建混合对象。例如，先生成运动鞋和T恤的混合图像，然后生成汽车和飞机的混合图像。
### 报告要求
在项目结束时，你需要撰写一份适当长度的报告，可能至少需要半页。在报告中，你应该描述你是如何完成任务的。具体包括：
- 遇到的困难（由于方法导致的，例如“训练样本不足以收敛”，而不是技术上的问题如“无法通过pip安装包”）。
- 采取的缓解困难的步骤。
- 对你所做工作的总体描述，解释你是如何理解任务的，以及你为解决任务所做的工作，用通俗语言描述，无需代码。
- 你方法的潜在局限性，可能存在的问题，以及在不同数据或稍有不同的条件下可能会遇到的困难。
- 如果你有如何扩展这个项目的有趣想法，也请描述一下。

在这个项目中，你将尝试使用CycleGAN将马的图像转换成猫的图像。由于这是一个较为复杂的任务，项目中已经提供了大量的代码，但你仍需要添加一些代码并进行训练和评估。
### 任务详情：
1. **添加训练Cycle GAN所需的代码**：
    - 完善数据加载器（data loaders）等必要的代码部分，以便能够加载和预处理马和猫的图像数据集。
    - 确保数据加载器能够处理图像数据并将其转换为适合CycleGAN模型训练的格式。
2. **训练和优化Cycle GAN**：
    - 训练CycleGAN模型，使其能够将马的图像转换成猫的图像，并能将转换后的猫图像还原为马图像。
    - 优化模型的超参数（如学习率、批量大小等），从小分辨率图像开始训练，以逐步了解模型的行为和超参数的影响。
    - 训练过程中需要监控损失函数，并根据损失值调整训练策略。
3. **可视化生成的图像**：
    - 生成并展示一些转换后的图像样本，展示从马图像转换成猫图像的效果。
    - 由于缺乏定量评估指标，主要通过定性评估生成图像的质量。
### 报告要求
在项目结束时，你需要撰写一份适当长度的报告，可能至少需要半页。在报告中，你应该描述你是如何完成任务的。具体包括：
- **遇到的困难**：描述在方法上遇到的困难，例如“训练样本不足以收敛”，而不是技术上的问题如“无法通过pip安装包”。
- **采取的缓解困难的步骤**：描述你为解决这些困难所采取的措施。
- **总体描述**：对你所做工作的总体描述，解释你是如何理解任务的，以及你为解决任务所做的工作，用通俗语言描述，无需代码。
- **潜在局限性**：描述你方法的潜在局限性，可能存在的问题，以及在不同数据或稍有不同的条件下可能会遇到的困难。
- **扩展想法**：如果你有如何扩展这个项目的有趣想法，也请描述一下。
