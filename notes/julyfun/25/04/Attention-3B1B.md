- 考虑:
    - mole 一词在不同上下文有不同含义.
    - 嵌入层将 mole 转换为泛型向量以后，Transformer 的下一层会**根据上下文再加一个偏移向量**。
	![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250428220412.png)

- $E_1^->$ 是词嵌入 $+$ 位置嵌入
- $Q_i^-> = W_Q dot E_i^->$  形象比喻：$E_1^->$ 是第四个单词，且是名词。问在第四个单词前面有形容词不？
- $K_i^-> = W_k dot E_i^->$ 形象比喻：$E_2^->$ 是第二个单词，形容词。（可以回答上面的询问）
- 上面这张表叫做 Attention Pattern。左下角掩码强制置 0，这样前面 Qi 查不到后面 Ki.
![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250428220719.png)
![image.png|500](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250428220832.png)
- $V_i^-> = W_v dot E_i^->$  表示对其他词应该造成什么偏置。比如上图从 creature 到蓝色毛茸茸生物的箭头.
