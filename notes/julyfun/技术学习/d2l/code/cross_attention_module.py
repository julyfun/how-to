import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class CrossAttention(nn.Module):
    """
    交叉注意力模块实现
    
    query, key, value 来自不同的数据源：
    - query: 通常来自解码器层
    - key, value: 通常来自编码器层的输出
    """
    def __init__(self, d_model, n_heads, dropout=0.1):
        super(CrossAttention, self).__init__()
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # 每个头的维度
        
        # 定义线性投影层
        self.query_proj = nn.Linear(d_model, d_model)
        self.key_proj = nn.Linear(d_model, d_model)
        self.value_proj = nn.Linear(d_model, d_model)
        self.output_proj = nn.Linear(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)
        
    def split_heads(self, x, batch_size):
        """
        分割最后一个维度到 (n_heads, d_k)
        """
        # 将形状从 (batch_size, seq_len, d_model) 转换为 
        # (batch_size, seq_len, n_heads, d_k)
        x = x.view(batch_size, -1, self.n_heads, self.d_k)
        # 转置为 (batch_size, n_heads, seq_len, d_k)
        return x.transpose(1, 2)
        
    def forward(self, query, key, value, mask=None):
        """
        实现交叉注意力前向传播
        
        Args:
            query: 查询张量 (batch_size, query_len, d_model)
            key: 键张量 (batch_size, key_len, d_model)
            value: 值张量 (batch_size, key_len, d_model)
            mask: 注意力掩码张量 (batch_size, 1, query_len, key_len) 或 (batch_size, query_len, key_len)
        """
        batch_size = query.size(0)
        
        # 1. 线性投影
        query = self.query_proj(query)  # (batch_size, query_len, d_model)
        key = self.key_proj(key)        # (batch_size, key_len, d_model)
        value = self.value_proj(value)  # (batch_size, key_len, d_model)
        
        # 2. 分割多头
        query = self.split_heads(query, batch_size)  # (batch_size, n_heads, query_len, d_k)
        key = self.split_heads(key, batch_size)      # (batch_size, n_heads, key_len, d_k)
        value = self.split_heads(value, batch_size)  # (batch_size, n_heads, key_len, d_k)
        
        # 3. 缩放点积注意力
        # 计算注意力分数
        scores = torch.matmul(query, key.transpose(-2, -1))  # (batch_size, n_heads, query_len, key_len)
        scores = scores / torch.sqrt(torch.tensor(self.d_k, dtype=torch.float32))
        
        # 应用注意力掩码(如果提供)
        if mask is not None:
            # 确保掩码形状兼容多头
            if mask.dim() == 3:
                mask = mask.unsqueeze(1)  # (batch_size, 1, query_len, key_len)
                
            # 将掩码中的0位置填充为负无穷
            scores = scores.masked_fill(mask == 0, -1e9)
        
        # 应用softmax获取注意力权重
        attention_weights = F.softmax(scores, dim=-1)  # (batch_size, n_heads, query_len, key_len)
        attention_weights = self.dropout(attention_weights)
        
        # 4. 加权求和
        context = torch.matmul(attention_weights, value)  # (batch_size, n_heads, query_len, d_k)
        
        # 5. 拼接多头输出
        # 转置回 (batch_size, query_len, n_heads, d_k)
        context = context.transpose(1, 2)
        # 合并多头 (batch_size, query_len, d_model)
        context = context.reshape(batch_size, -1, self.d_model)
        
        # 6. 最终输出投影
        output = self.output_proj(context)  # (batch_size, query_len, d_model)
        
        return output, attention_weights

# 演示代码
def demo():
    """
    演示如何使用CrossAttention模块
    """
    # 设置随机种子确保可复现
    torch.manual_seed(42)
    
    # 设置参数
    batch_size = 2
    query_len = 4  # 目标序列长度
    key_len = 6    # 源序列长度
    d_model = 64   # 模型维度
    n_heads = 8    # 多头数量
    
    # 创建模型
    cross_attn = CrossAttention(d_model, n_heads)
    
    # 创建输入
    query = torch.randn(batch_size, query_len, d_model)
    key = torch.randn(batch_size, key_len, d_model)
    value = torch.randn(batch_size, key_len, d_model)
    
    # 创建掩码 (例如: 填充掩码)
    mask = torch.ones(batch_size, query_len, key_len)
    mask[:, :, -2:] = 0  # 掩盖最后两个位置
    
    # 计算注意力
    output, attention_weights = cross_attn(query, key, value, mask)
    
    print(f"输入维度:")
    print(f"  Query: {query.shape}")
    print(f"  Key/Value: {key.shape} / {value.shape}")
    print(f"  Mask: {mask.shape}")
    print(f"\n输出维度:")
    print(f"  输出: {output.shape}")
    print(f"  注意力权重: {attention_weights.shape}")
    
    # 访问某个头的注意力权重
    head_idx = 0
    print(f"\n第{head_idx+1}个头的注意力权重 (带掩码):")
    print(attention_weights[0, head_idx])

if __name__ == "__main__":
    demo() 
