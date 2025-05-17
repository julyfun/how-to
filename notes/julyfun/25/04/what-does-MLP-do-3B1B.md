
![image.png|600](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250518022638.png)
- 结构: Linear + ReLU + Linear
	- 假设 Attention 输出的 $E^->$ 嵌入维度 10000
	- 前半 Linear 矩阵 30000x10000:
		- ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250518022827.png)
		- [e.g.] 第一行 $R_0^->$ 通过点乘查询：这个 $E^->$ 是否编码了“Michael Jordan” 的含义？（可包含多个含义）
		- [e.g.] 第二行 $R_1^->$ 通过点乘查询：这个 $E^->$ 是否编码了四足动物的含义？
		- 后面还有 Bais，每个元素修正一个查询结果. 例如通过 -1 来让第一个点积由 2 变成 1.
	- 中间 ReLU 层:
		- ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250518023507.png)
		- 将前面小于 0 的结果直接变 0. 即把大于 0 当作 active，小于 0 当作 inactive.
		- 结果升维了，不再是嵌入空间，而是类似于“每一个元素代表一个查询结果”.
	- 后半 Linear 层例如 30000x10000，一定和前半相反:
		- ![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250518023712.png)
		- [e.g.] 第一列可以理解为一个嵌入空间中的向量，将第一个查询结果转换为**嵌入空间**的向量. 如 $C_0$ 可能在嵌入空间中包含“篮球，数字23”等多个意思！
		- 偏置向量可以理解为直接暴力加在结果后的嵌入向量！我靠，难道意味着一次 MLP 会植入一个信号么?
- 最后通过残差层，将结果加入到开始的输入上. 如最上面的图.
