== 采集原始数据
+ 左右手 absolute pose (e.g. 在 vive tracker 世界坐标系或 ARKit 初始坐标系)
+ 左右手相机图像.
+ 头部 absolute pose
+ 头部相机图像

== 假设
+ 左右手 TCP 原点位于 end-effector 的同一个点. Rotation 的 y 轴相反（为了手性一致），xz 轴一致.
  + 若左右手硬件对称而手性相反，则 TCP 原点处于对称位置.
+ 左右相机相对于各自 TCP 的 transform 左右对称，x 轴相反（为了手性一致），yz 轴一致. 左右相机的水平方向在对称前提下可以任意旋转.
+ 机器人左右对称.
+ 左右手需要转换为 TCP pose，头部 pose 需要转为为相机 pose. （Vive tracker 原始数据可能是 tracker pose，因此需要转换）

== 目标
将采集数据增强为镜像数据, s.t. 镜像数据等价于原始采集环境中把环境按照机器人的中轴平面镜像设置，动作也镜像，但坐标系不镜像，采集得到的数据（包括输入的 image 正确，以及产生的 GT *relative* action 正确）

== action pose 如何处理？
=== 方法 I
对于 absolute pose 直接右乘 $"diag"(1, -1, 1, 1)$

=== 方法 II
先转换为 chunk relative pose，然后对每个 relative pose T 计算 $"diag"$
