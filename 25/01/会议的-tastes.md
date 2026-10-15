---
title: "会议的 tastes"
date: 2025-01-01 16:31:55
tags: ["25", "01"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 27.0.0 Darwin Kernel Version 27.0.0: Tue Aug 11 21:02:59 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

下面的 **taste 是对历年论文取向的概括**；写作风格是相应的投稿建议。代表作跨年份选择并标注会议届年；部分标题采用常用简称；每篇贡献均为一句且不含逗号。

| 会议 | Taste 一句话 | 偏好的写作风格一句话 |
|---|---|---|
| **RSS** | 看重机器人问题中的深刻洞见以及由此带来的能力突破。 | 围绕一个核心洞见组织全文并用严谨分析或扎实机器人实验建立完整证据链。 |
| **CoRL** | 看重学习方法如何提升机器人的泛化能力与数据效率。 | 清楚交代学习问题和数据设置并用公平基线与泛化实验说明提升来自哪里。 |
| **NeurIPS** | 看重对广泛学习问题具有影响力的新方法与新认识。 | 把贡献提炼成可推广的学习命题并用理论或系统实验界定结论的适用范围。 |
| **ICML** | 看重机器学习方法在建模与优化及统计层面的实质进展。 | 精确定义问题和假设并让算法推导与实验验证形成紧密对应。 |
| **ICLR** | 看重表征与模型结构及训练机制中简洁有效的新思想。 | 用直观动机引出核心设计并用针对性消融解释为什么有效。 |
| **CVPR** | 看重视觉任务上的明确突破以及可复用的方法或数据资源。 | 用清晰方法图与充分定量比较及直观可视化证明视觉能力的提升。 |
| **ICCV** | 看重具有广泛影响的视觉方法与对视觉问题的新理解。 | 从视觉问题本身建立动机并用跨任务证据与深入分析支撑方法的普适价值。 |
| **ICRA** | 看重机器人算法与硬件及系统对实际问题的可靠解决。 | 明确工程约束和技术贡献并报告精度与运行效率及实机表现。 |
| **IROS** | 看重智能机器人在复杂环境中的感知与行动及系统集成能力。 | 从具体场景出发交代系统设计并用多场景实验和失败分析证明实用性。 |
| **ECCV** | 看重视觉建模中的结构性创新与扎实的实验洞察。 | 把建模选择讲透并通过受控实验与可视化解释性能变化的原因。 |
| **AAAI** | 看重能推进学习与推理及规划等人工智能能力的明确贡献。 | 面向广泛 AI 读者清楚定义问题并以紧凑论证和充分比较突出方法价值。 |
| **IJCAI** | 看重具有一般意义的智能问题及其算法或理论解决方案。 | 从形式化问题出发说明方法的新颖性并用理论性质或系统实验支持结论。 |
| **HRI** | 看重机器人如何影响人的理解与信任及协作行为。 | 围绕研究问题组织交互设计与用户研究并严谨报告测量和统计结果。 |
| **ISRR** | 看重能够推动机器人研究方向的深层思想与成熟研究成果。 | 用连贯论述讲清问题背后的原理并把方法细节与长期意义充分展开。 |

**RSS｜代表作 3 篇**

- [Diffusion Policy（2023）](https://roboticsproceedings.org/rss19/p026.pdf)：通过对动作序列进行条件扩散建模实现能够表达多模态行为的视觉操作策略。
- [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware／ACT（2023）](https://www.roboticsproceedings.org/rss19/p016.pdf)：结合低成本双臂遥操作系统与动作分块 Transformer 实现少量示范下的精细双臂操作。
- [ElasticFusion（2015）](https://roboticsproceedings.org/rss11/p01.html)：通过表面元素融合与非刚性地图变形实现无需位姿图的实时稠密 RGB-D SLAM。

**CoRL｜代表作 3 篇**

- [Transporter Networks（2020）](https://proceedings.mlr.press/v155/zeng21a.html)：通过搬运视觉特征预测空间动作实现具有较高示范效率的机器人拾放操作。
- [Perceiver-Actor／PerAct（2022）](https://proceedings.mlr.press/v205/shridhar23a.html)：通过语言条件下的体素动作预测学习覆盖多种六自由度操作任务的统一策略。
- [R3M（2022）](https://proceedings.mlr.press/v205/nair23a.html)：从人类视频中预训练可迁移视觉表征以降低机器人操作策略对示范数据的需求。

**NeurIPS｜代表作 3 篇**

- [AlexNet（2012）](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)：通过 GPU 训练的深层卷积网络大幅提升大规模图像分类性能。
- [Attention Is All You Need（2017）](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)：提出以注意力为核心的 Transformer 架构实现高效并行的序列建模。
- [Denoising Diffusion Probabilistic Models／DDPM（2020）](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)：通过学习逐步去噪的逆扩散过程实现高质量图像生成。

**ICML｜代表作 3 篇**

- [Trust Region Policy Optimization／TRPO（2015）](https://proceedings.mlr.press/v37/schulman15.pdf)：通过限制策略更新幅度构建具有理论改进依据的稳定策略优化方法。
- [SimCLR（2020）](https://proceedings.mlr.press/v119/chen20j)：通过数据增强与对比学习在无需人工标签的条件下学习高质量视觉表征。
- [CLIP（2021）](https://proceedings.mlr.press/v139/radford21a.html)：通过大规模图文对比预训练实现由自然语言指定类别的零样本图像识别。

**ICLR｜代表作 3 篇**

- [Auto-Encoding Variational Bayes／VAE（2014）](https://arxiv.org/abs/1312.6114)：通过重参数化技巧实现潜变量生成模型的高效随机梯度训练。
- [Adam（2015）](https://arxiv.org/abs/1412.6980)：利用梯度的一阶与二阶矩估计实现逐参数自适应的随机优化。
- [LoRA（2022）](https://openreview.net/forum?id=nZeVKeeFYf9)：通过训练低秩权重增量显著降低大语言模型适配所需的可训练参数量。

**CVPR｜代表作 3 篇**

- [Fully Convolutional Networks／FCN（2015）](https://openaccess.thecvf.com/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html)：将分类网络改造为全卷积网络以实现端到端的像素级语义分割。
- [Deep Residual Learning／ResNet（2016）](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)：通过残差连接缓解深层网络的优化困难并使更深的视觉模型有效训练。
- [You Only Look Once／YOLO（2016）](https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html)：将目标检测统一为单次网络前向计算以实现实时检测。

**ICCV｜代表作 3 篇**

- [Mask R-CNN（2017）](https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html)：通过加入掩码预测分支与 RoIAlign 将目标检测扩展为高精度实例分割。
- [Swin Transformer（2021）](https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.html)：通过层次结构与移位窗口注意力构建计算高效的通用视觉骨干网络。
- [Segment Anything／SAM（2023）](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html)：通过可提示分割模型与大规模掩码数据实现对新图像的零样本分割迁移。

**ICRA｜代表作 3 篇**

- [RRT-Connect（2000）](https://lavalle.pl/sbplan.html)：通过双向随机树的贪心连接加速高维空间中的单次查询运动规划。
- [CHOMP（2009）](https://publications.ri.cmu.edu/chomp-gradient-optimization-techniques-for-efficient-motion-planning)：通过协变梯度优化将初始轨迹改进为平滑且避障的机器人运动轨迹。
- [Anytime Motion Planning Using the RRT*（2011）](https://people.csail.mit.edu/teller/pubs/KaramanEtAl_ICRA_2011.pdf)：将 RRT* 扩展为能够在执行过程中持续改进路径质量的实时规划方法。

**IROS｜代表作 3 篇**

- [Informed RRT*（2014）](https://robotic-esp.com/papers/gammell_iros14)：通过直接采样可能改善当前路径的椭球区域加速最优运动规划的收敛。
- [Domain Randomization（2017）](https://arxiv.org/abs/1703.06907)：通过随机化仿真视觉条件使仅用合成图像训练的模型迁移到真实机器人场景。
- [LIO-SAM（2020）](https://researchwith.stevens.edu/en/publications/lio-sam-tightly-coupled-lidar-inertial-odometry-via-smoothing-and/)：通过因子图紧耦合激光雷达与惯性测量实现实时里程计和地图构建。

**ECCV｜代表作 3 篇**

- [Spatial Pyramid Pooling／SPP-net（2014）](https://people.csail.mit.edu/kaiming/index.html)：通过空间金字塔池化将不同尺寸图像转换为固定长度特征并减少检测中的重复卷积计算。
- [End-to-End Object Detection with Transformers／DETR（2020）](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460205.pdf)：通过集合预测与二分图匹配实现无需手工锚框和非极大值抑制的端到端目标检测。
- [RAFT（2020）](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/3526_ECCV_2020_paper.php)：通过全像素对相关体与循环更新实现高精度且泛化能力强的光流估计。

**AAAI｜代表作 3 篇**

- [D* Lite（2002）](https://aaai.org/papers/00476-aaai02-072-d-lite/)：通过复用已有搜索结果实现环境变化后的高效最短路径重规划。
- [Deep Reinforcement Learning with Double Q-Learning（2016）](https://ojs.aaai.org/index.php/AAAI/article/view/10295)：通过分离动作选择与价值评估减少 DQN 的价值过估计并提升控制性能。
- [Rainbow（2018）](https://cdn.aaai.org/ojs/11796/11796-13-15324-1-2-20201228.pdf)：整合六种互补的 DQN 改进并通过消融验证其对数据效率和最终性能的贡献。

**IJCAI｜代表作 3 篇**

- [ICBS（2015）](https://www.ijcai.org/Proceedings/15/Papers/110.pdf)：通过冲突优先级与合并重启等机制加速保持最优性的多智能体路径搜索。
- [Network Representation Learning with Rich Text Information／TADW（2015）](https://www.ijcai.org/Abstract/15/299)：将 DeepWalk 解释为矩阵分解并融入节点文本信息以提升网络表征质量。
- [Multilingual Knowledge Graph Embeddings／MTransE（2017）](https://www.ijcai.org/proceedings/2017/209)：通过学习不同语言知识图谱嵌入空间之间的映射实现跨语言实体与关系对齐。

**HRI｜代表作 3 篇**

- [Legibility and Predictability of Robot Motion（2013）](https://personalrobotics.cs.washington.edu/publications/dragan2013legibility/)：区分动作可预测性与意图可读性并提出让人更容易推断机器人目标的运动设计方法。
- [Would You Trust a (Faulty) Robot?（2015）](https://uhra.herts.ac.uk/id/eprint/14116/3/2696454_2696497.pdf)：通过用户实验揭示机器人错误对主观信任的影响与实际服从行为并不完全一致。
- [Overtrust of Robots in Emergency Evacuation Scenarios（2016）](https://sites.cc.gatech.edu/~alanwags/pubs/Robinette-HRI-2016.pdf)：通过疏散实验发现参与者可能在观察到机器人先前失误后仍过度依赖其引导。

**ISRR｜代表作 3 篇**

- [Learning Movement Primitives（2003）](https://www-live.dfki.de/en/web/research/projects-and-publications/publication/13965)：将动态运动基元组织为支持示范学习与在线调整及强化学习改进的模块化运动控制框架。
- [Realtime Informed Path Sampling for Motion Planning Search（2011）](https://www.ri.cmu.edu/publications/realtime-informed-path-sampling-for-motion-planning-search/)：利用碰撞检测反馈在线建立障碍概率模型以提高运动规划中的有效路径采样率。
- [Path Planning with Loop Closure Constraints Using an Atlas-Based RRT（2011）](https://www.iri.upc.edu/publications/show/1250)：通过联合构建约束流形图册与随机树提高闭链机器人系统的运动规划效率。

