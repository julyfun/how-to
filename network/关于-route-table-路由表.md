- reliability: "20% (author)"
- date: 2024-10-10
- os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# 关于 Route Table 路由表

简单 route table 网络是一颗有根树，叶子结点为电脑，非叶子结点为路由器。任何节点的默认网关为其父亲。非叶子节点 u 对于子树中所有非叶子结点 v，需要指定 u -> v 路径上的第一个点，不然就传不了。

如要避免上层非叶子节点存储的路由过多，需要设计子网分段。

