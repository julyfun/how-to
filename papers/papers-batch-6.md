---
title: "papers batch 6"
date: 2026-07-06 18:12:51
tags: ["papers"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

to read:

## lingbot-vla 2.0: From Foundation to Application: Improving VLA Models in Practice
[Gemini 3.1 Pro] 引入无辅助损失的 MoE 架构，并通过附加查询 token 蒸馏几何和时序特征 | 👤 Ant Digital Technologies, Wei Wu, Kecheng Zheng | [🌐](-) | [📃 2607.06403](https://hjfy.top/arxiv/2607.06403) | [✨](https://www.alphaxiv.org/abs/2607.06403) | [📂](-) |

相比前作扩大了涵盖 20 种具身和人类主视角视频的预训练数据，将动作空间统一为包含全身关节的 55 维向量。模型在动作专家中引入无辅助损失的 token 级 MoE 架构，并附加当前和未来时间步的查询 token 向深度估计模型和因果视频模型蒸馏几何和时序特征。

消融实验表明相对关节动作比绝对关节动作表现更好，均值标准差归一化能保留更大的有效动态范围。接触丰富的末端运动在笛卡尔空间表现更好，受姿态约束的任务在关节空间表现更好。

## PaLM-E: An Embodied Multimodal Language Model
[Gemini 3.1 Pro] PaLM-E 将连续传感器数据直接映射到预训练语言模型的嵌入空间来实现具身推理 | 👤 Robotics at Google 和 TU Berlin, Danny Driess, Danny Driess 和 Pete Florence | [🌐](https://palm-e.github.io/) | [📃 2303.03378](https://hjfy.top/arxiv/2303.03378) | [✨](https://www.alphaxiv.org/abs/2303.03378) | - |

PaLM-E 将图像和状态数据通过编码器映射为向量，与文本 token 交错拼接成多模态句子，直接输入给预训练的 PaLM 模型自回归生成高层控制文本。

实验发现混合训练视觉语言和机器人数据能提升单任务表现，并且扩大语言模型参数量可以显著减少多模态训练对原有语言能力的灾难性遗忘。

## SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation
[Gemini 3.1 Pro] 结合基于动作原语的阶段估计器和多门控混合专家价值头来提供密集多任务奖励 | 👤 Stanford University, Qianzhong Chen, Mac Schwager | [🌐](https://qianzhong-chen.github.io/sarm2.github.io/) | [📃 2606.10305](https://hjfy.top/arxiv/2606.10305) | [✨](https://www.alphaxiv.org/abs/2606.10305) | [📂](https://qianzhong-chen.github.io/sarm2.github.io/) |

提出多任务阶段感知奖励模型 RM。它结合了基于动作原语的阶段估计器和混合专家价值头，能为操作任务提供单步密集奖励并据此指导机器人利用自主数据迭代策略。

## ActiveGlasses: Learning Manipulation with Active Vision from Ego-centric Human Demonstration
[Gemini 3.1 Pro] 利用智能眼镜记录人类演示提取对象轨迹，联合预测操作与头部运动以实现主动视觉的零样本迁移 | 👤 Shanghai Jiao Tong University, Yanwen Zou, Cewu Lu | - | [📃 2604.08534](https://hjfy.top/arxiv/2604.08534) | [✨](https://www.alphaxiv.org/abs/2604.08534) | - |

提出直接使用安装在智能眼镜上的双目摄像头收集人类演示。部署时将相机安装在感知机械臂上，使用以物体为中心的点云策略联合预测机器人的操作和相机运动以复现人类的主动视觉。

## VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs
[Gemini 3.1 Pro] 通过轻量级模态迁移微调和触觉正则化损失将触觉流接入预训练的视频动作模型中 | 👤 Virginia Tech, Haoran Yuan, Ismini Lourentzou | [🌐](https://plan-lab.github.io/projects/vtam/) | [📃 2603.23481](https://hjfy.top/arxiv/2603.23481) | [✨](https://www.alphaxiv.org/abs/2603.23481) | [📂](https://plan-lab.github.io/projects/vtam/) |

提出一种结合了触觉感知的视频触觉动作模型 VTAM。该方法通过轻量级模态迁移微调将触觉流直接增强到预训练视频动作模型中，并引入触觉正则化损失强制平衡跨模态注意力以防止视觉主导。

## RoboPocket: Improve Robot Policies Instantly with Your Phone
[Gemini 3.1 Pro] 利用智能手机的 AR 视觉预见发现策略失败区域并基于此通过异步在线微调闭环快速迭代策略 | 👤 Shanghai Jiao Tong University, Junjie Fang, Cewu Lu | [🌐](https://robo-pocket.github.io) | [📃 2603.05504](https://hjfy.top/arxiv/2603.05504) | [✨](https://www.alphaxiv.org/abs/2603.05504) | [📂](https://robo-pocket.github.io) |

提出了一个基于普通智能手机的数据收集与微调系统。操作员利用手机远程推理和 AR 视觉预见直观看到策略预测轨迹，从而发现并针对策略薄弱区收集数据，最后通过异步在线微调持续更新策略。

## Rethinking Camera Choice: An Empirical Study on Fisheye Camera Properties in Robotic Manipulation
[Gemini 3.1 Pro] 探究了腕部鱼眼相机的空间定位与泛化特性并发现简单随机缩放增强能改善硬件泛化 | 👤 Shanghai Jiao Tong University, Han Xue, Chuan Wen | [🌐](https://robo-fisheye.github.io/) | [📃 2603.02139](https://hjfy.top/arxiv/2603.02139) | [✨](https://www.alphaxiv.org/abs/2603.02139) | [📂](https://robo-fisheye.github.io/) |

对机器人操作中使用的腕部鱼眼相机进行了实证研究。作者发现鱼眼相机的宽视野在复杂环境中能提升空间定位能力，并在环境多样性充足时解锁出色的场景泛化。

跨相机的规模过拟合问题可通过随机缩放增强解决。

## Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations
[Gemini 3.1 Pro] 利用便携式硬件捕捉人类动作并通过分层学习管道转化为人形机器人全身操作技能 | 👤 Tsinghua University, Ruiqian Nai, Yang Gao | [🌐](https://humanoid-manipulation-interface.github.io) | [📃 2602.06643](https://hjfy.top/arxiv/2602.06643) | [✨](https://www.alphaxiv.org/abs/2602.06643) | [📂](https://humanoid-manipulation-interface.github.io) |

提出用于人形机器人全身操作的 HuMI 框架。该框架使用便携式硬件捕捉无机器人的丰富人类全身运动数据，随后通过分层学习管道将人类动作转化为人形机器人灵巧可行的操作技能。

## From Digital to Physical: Digital Agents as Autonomous Coaches for Physical Intelligence
[Gemini 3.1 Pro] 利用大语言模型智能体基于可执行代码接口和环境反馈自主迭代设计奖励与架构 | 👤 Shanghai Jiao Tong University, Zixing Lei, Siheng Chen | - | [📃 2601.21570](https://hjfy.top/arxiv/2601.21570) | [✨](https://www.alphaxiv.org/abs/2601.21570) | - |

提出了 EmboCoach-Bench 框架。该框架将可执行代码作为接口，利用大语言模型智能体根据环境反馈自主进行闭环工程，从而迭代起草和优化诸如强化学习的奖励设计以及扩散策略架构。

## Translating Flow to Policy via Hindsight Online Imitation
[Gemini 3.1 Pro] 收集在线交互数据并通过事后重新标注高层目标结果来更新目标条件的动作模仿策略 | 👤 Tsinghua University, Yitian Zheng, Yang Gao | - | [📃 2512.19269](https://hjfy.top/arxiv/2512.19269) | [✨](https://www.alphaxiv.org/abs/2512.19269) | - |

提出 HinFlow 方法。它利用高层规划器生成的二维点流作为指导，通过收集在线交互数据从事后达成结果中重新标注目标，最后聚合这些数据来更新目标条件的底层模仿策略。

## ImplicitRDP: An End-to-End Visual-Force Diffusion Policy with Structural Slow-Fast Learning
[Gemini 3.1 Pro] 利用因果注意力同步处理慢视觉和快力觉 token 并用虚拟目标表示正则化防止模态崩溃 | 👤 Shanghai Jiao Tong University, Wendi Chen, Cewu Lu | [🌐](https://implicit-rdp.github.io) | [📃 2512.10946](https://hjfy.top/arxiv/2512.10946) | [✨](https://www.alphaxiv.org/abs/2512.10946) | [📂](https://implicit-rdp.github.io) |

提出了端到端视觉力觉扩散策略 ImplicitRDP。方法引入了结构化慢快学习机制并利用因果注意力处理异步的视觉与力觉 token，同时通过基于虚拟目标的表示正则化将力觉映射到动作空间中。

## Maestro: Orchestrating Robotics Modules with Vision-Language Models for Zero-Shot Generalist Robots
[Gemini 3.1 Pro] 利用视觉语言模型动态组合现有感知与控制模块来直接生成针对当前任务的代码策略 | 👤 University of Pennsylvania, Junyao Shi, Dinesh Jayaraman | - | [📃 2511.00917](https://hjfy.top/arxiv/2511.00917) | [✨](https://www.alphaxiv.org/abs/2511.00917) | - |

提出了 Maestro 智能体框架。该系统不训练端到端模型，而是让充当代码编写者的视觉语言模型动态组合预先构建的各种感知和控制模块，从而生成适用于当前场景的编程式闭环策略。

## ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation
[Gemini 3.1 Pro] 利用在线故障检测算法自主判断何时需要人类介入共享控制以高效收集领域内数据 | 👤 Shanghai Jiao Tong University, Wenye Yu, Cewu Lu | - | [📃 2510.02298](https://hjfy.top/arxiv/2510.02298) | [✨](https://www.alphaxiv.org/abs/2510.02298) | - |

设计了多机器人部署与适应系统 ARMADA。其核心在于引入了在线故障检测方法 FLOAT，使得系统能在并行展开策略时仅在必要时请求人类干预，以此减少人类监控负担并获取部署数据。

## TimeRewarder: Learning Dense Reward from Passive Videos via Frame-wise Temporal Distance
[Gemini 3.1 Pro] 通过建模被动视频帧对之间的时间距离来估计任务完成进度作为强化学习密集代理奖励 | 👤 Tsinghua University, Yuyang Liu, Yang Gao | - | [📃 2509.26627](https://hjfy.top/arxiv/2509.26627) | [✨](https://www.alphaxiv.org/abs/2509.26627) | - |

提出了简单的奖励学习方法 TimeRewarder。该方法利用无动作的被动视频，通过对视频帧对之间的时间距离进行建模以估计操作朝向任务完成的进度，最终将其作为强化学习的单步密集奖励。

## SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration
[Gemini 3.1 Pro] 学习任务相关因素的紧凑表示并将策略探索严格限制在有效动作的流形空间上 | 👤 Shanghai Jiao Tong University, Yang Jin, Cewu Lu | [🌐](https://ericjin2002.github.io/SOE) | [📃 2509.19292](https://hjfy.top/arxiv/2509.19292) | [✨](https://www.alphaxiv.org/abs/2509.19292) | [📂](https://ericjin2002.github.io/SOE) |

提出用于策略自我改进的 SOE 框架。该方法学习了任务相关因素的潜在表示并将探索限制在有效动作的流形空间内，避免了随机扰动带来的不安全行为，能作为插件集成到任意策略中。

## MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies
[Gemini 3.1 Pro] 收集人类 VR 数据并通过加权协同训练将其运动知识迁移给端到端机器人部署策略 | 👤 Tsinghua University, Chengbo Yuan, Yang Gao | [🌐](https://motiontrans.github.io/) | [📃 2509.17759](https://hjfy.top/arxiv/2509.17759) | [✨](https://www.alphaxiv.org/abs/2509.17759) | [📂](https://motiontrans.github.io/) |

提出了多任务人机协同训练框架 MotionTrans。该系统通过数据收集和人类数据转换管道，利用加权的协同训练策略直接将人类示范中的丰富运动知识转移到最终的端到端机器人操作策略上。

实验表明成功的关键在于必须与机器人数据协同训练，且需要广泛覆盖与任务相关的运动。

## Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization
[Gemini 3.1 Pro] 通过混合位置力控制器将 VLM 与触觉感知相连以激活预训练模型中的物理交互知识 | 👤 Tsinghua University, Jialei Huang, Yang Gao | - | [📃 2507.09160](https://hjfy.top/arxiv/2507.09160) | [✨](https://www.alphaxiv.org/abs/2507.09160) | - |

提出了 Tactile-VLA 框架。该方法将视觉、语言和触觉传感深度融合，通过混合位置力控制器将模型意图转化为物理动作，并使用推理模块让机器人根据触觉反馈调整策略，只需少量演示就能激活模型的物理先验。

