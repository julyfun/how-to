import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子以确保结果可复现
torch.manual_seed(42)

# 演示自注意力机制的基本计算过程
def self_attention_demo(query, key, value):
    """
    演示自注意力机制的计算步骤
    """
    # 计算注意力分数 (Q·K^T)
    scores = torch.matmul(query, key.transpose(-2, -1))
    
    # 缩放注意力分数
    d_k = key.size(-1)
    scaled_scores = scores / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    
    # 应用 softmax 获取注意力权重
    weights = F.softmax(scaled_scores, dim=-1)
    
    # 计算输出 (weights·V)
    output = torch.matmul(weights, value)
    
    return output, weights

# 演示交叉注意力机制
def cross_attention_demo(query, key, value, mask=None):
    """
    演示交叉注意力机制和注意力掩码的使用
    
    Args:
        query: 查询张量 (batch_size, query_len, d_model)
        key: 键张量 (batch_size, key_len, d_model)
        value: 值张量 (batch_size, key_len, d_model)
        mask: 注意力掩码张量 (batch_size, query_len, key_len)
    """
    # 计算注意力分数
    scores = torch.matmul(query, key.transpose(-2, -1))
    
    # 缩放注意力分数
    d_k = key.size(-1)
    scaled_scores = scores / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    
    # 应用注意力掩码（如果提供）
    if mask is not None:
        # 将掩码中的0位置设为一个很大的负数，使softmax后的权重接近0
        scaled_scores = scaled_scores.masked_fill(mask == 0, -1e9)
    
    # 应用 softmax 获取注意力权重
    weights = F.softmax(scaled_scores, dim=-1)
    
    # 计算输出
    output = torch.matmul(weights, value)
    
    return output, weights, scaled_scores

# 可视化注意力权重
def visualize_attention(weights, title="Attention Weights"):
    """
    可视化注意力权重矩阵
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(weights.detach().numpy(), cmap="viridis")
    plt.colorbar()
    plt.title(title)
    plt.xlabel("Key positions")
    plt.ylabel("Query positions")
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    plt.close()

# 主函数，展示交叉注意力和注意力掩码的工作原理
def main():
    print("演示交叉注意力和注意力掩码的工作原理")
    
    # 设定参数
    batch_size = 1
    query_len = 4
    key_len = 6
    d_model = 8
    
    # 创建随机输入数据
    query = torch.randn(batch_size, query_len, d_model)
    key = torch.randn(batch_size, key_len, d_model)
    value = torch.randn(batch_size, key_len, d_model)
    
    print(f"Query shape: {query.shape}")
    print(f"Key shape: {key.shape}")
    print(f"Value shape: {value.shape}")
    
    # 1. 不使用掩码的交叉注意力
    print("\n1. 不使用掩码的交叉注意力:")
    output, weights, scores = cross_attention_demo(query, key, value)
    print(f"注意力权重形状: {weights.shape}")
    print(f"输出形状: {output.shape}")
    
    # 可视化不带掩码的注意力权重
    visualize_attention(weights[0], "Cross Attention Without Mask")
    
    # 2. 使用掩码的交叉注意力（模拟序列填充掩码）
    print("\n2. 使用掩码的交叉注意力 (模拟序列填充掩码):")
    
    # 创建一个掩码，假设后两个key位置是填充的
    # 1表示关注，0表示忽略
    mask = torch.ones(batch_size, query_len, key_len)
    mask[:, :, -2:] = 0  # 将最后两个位置掩盖掉
    
    print(f"注意力掩码 (1=保留, 0=忽略):\n{mask[0]}")
    
    # 使用掩码计算注意力
    masked_output, masked_weights, masked_scores = cross_attention_demo(query, key, value, mask)
    
    print(f"掩码前的注意力分数:\n{scores[0]}")
    print(f"掩码后的注意力分数:\n{masked_scores[0]}")
    print(f"带掩码的注意力权重:\n{masked_weights[0]}")
    
    # 可视化带掩码的注意力权重
    visualize_attention(masked_weights[0], "Cross Attention With Mask")
    
    # 3. 对比带掩码和不带掩码的输出差异
    print("\n3. 对比带掩码和不带掩码的输出差异:")
    diff = torch.abs(output - masked_output)
    print(f"输出差异（L1范数）: {diff.sum().item()}")

if __name__ == "__main__":
    main() 
