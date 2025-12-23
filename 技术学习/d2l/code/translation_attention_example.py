import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

torch.manual_seed(42)

class SimpleCrossAttention(nn.Module):
    """
    简化版的交叉注意力机制，用于机器翻译可视化
    """
    def __init__(self):
        super(SimpleCrossAttention, self).__init__()
        
    def forward(self, query, key, value, mask=None):
        """
        Args:
            query: 目标语言的嵌入表示 (batch_size, tgt_len, d_model)
            key: 源语言的嵌入表示 (batch_size, src_len, d_model)
            value: 源语言的嵌入表示 (batch_size, src_len, d_model)
            mask: 注意力掩码 (batch_size, tgt_len, src_len)
        """
        # 计算注意力分数
        scores = torch.matmul(query, key.transpose(-2, -1))
        
        # 缩放分数
        d_k = key.size(-1)
        scaled_scores = scores / (d_k ** 0.5)
        
        # 应用掩码
        if mask is not None:
            scaled_scores = scaled_scores.masked_fill(mask == 0, -1e9)
        
        # 计算注意力权重
        attention_weights = F.softmax(scaled_scores, dim=-1)
        
        # 计算注意力输出
        output = torch.matmul(attention_weights, value)
        
        return output, attention_weights

def visualize_attention_weights(weights, src_tokens, tgt_tokens, title="Attention Weights"):
    """
    可视化注意力权重
    
    Args:
        weights: 注意力权重矩阵 (tgt_len, src_len)
        src_tokens: 源语言的单词
        tgt_tokens: 目标语言的单词
        title: 图的标题
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(weights.numpy(), 
                xticklabels=src_tokens,
                yticklabels=tgt_tokens,
                cmap='viridis',
                annot=True)
    plt.xlabel('Source Tokens')
    plt.ylabel('Target Tokens')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    plt.close()

def translation_example():
    """
    机器翻译中交叉注意力和注意力掩码的示例
    """
    print("===== 机器翻译中的交叉注意力演示 =====")
    
    # 简单的英语-中文翻译例子
    english_sentence = ["I", "love", "machine", "learning", "."]
    chinese_sentence = ["我", "喜欢", "机器", "学习", "。"]
    
    # 假设我们已经有了词嵌入
    # 模拟单词嵌入向量
    embed_dim = 8  # 嵌入维度
    
    # 创建简单的嵌入表示
    # 在实际应用中，这会来自预训练词嵌入或模型的嵌入层
    src_embeddings = {
        "I": torch.randn(embed_dim),
        "love": torch.randn(embed_dim),
        "machine": torch.randn(embed_dim),
        "learning": torch.randn(embed_dim),
        ".": torch.randn(embed_dim),
        "<pad>": torch.zeros(embed_dim)  # 填充标记
    }
    
    tgt_embeddings = {
        "我": torch.randn(embed_dim),
        "喜欢": torch.randn(embed_dim),
        "机器": torch.randn(embed_dim),
        "学习": torch.randn(embed_dim),
        "。": torch.randn(embed_dim),
        "<pad>": torch.zeros(embed_dim)  # 填充标记
    }
    
    # 情景1: 完整句子的翻译 (无掩码)
    src_tokens = english_sentence
    tgt_tokens = chinese_sentence
    
    # 创建词嵌入序列
    src_seq = torch.stack([src_embeddings[token] for token in src_tokens])
    tgt_seq = torch.stack([tgt_embeddings[token] for token in tgt_tokens])
    
    # 添加批次维度
    src_seq = src_seq.unsqueeze(0)  # [1, src_len, embed_dim]
    tgt_seq = tgt_seq.unsqueeze(0)  # [1, tgt_len, embed_dim]
    
    # 创建交叉注意力模型
    cross_attention = SimpleCrossAttention()
    
    # 计算不带掩码的注意力
    _, attention_weights = cross_attention(tgt_seq, src_seq, src_seq)
    
    # 可视化注意力
    print("\n情景1: 完整句子翻译 (无掩码)")
    print(f"源语言: {' '.join(src_tokens)}")
    print(f"目标语言: {' '.join(tgt_tokens)}")
    
    # 可视化注意力权重
    visualize_attention_weights(
        attention_weights[0], 
        src_tokens, 
        tgt_tokens, 
        "Translation Attention (No Mask)"
    )
    
    # 情景2: 含填充的句子翻译 (使用填充掩码)
    # 延长源句子并添加填充
    padded_src_tokens = english_sentence + ["<pad>", "<pad>"]
    
    # 创建填充的嵌入序列
    padded_src_seq = torch.stack([src_embeddings[token] for token in padded_src_tokens])
    padded_src_seq = padded_src_seq.unsqueeze(0)  # [1, padded_src_len, embed_dim]
    
    # 创建注意力掩码
    src_len = len(padded_src_tokens)
    tgt_len = len(tgt_tokens)
    attention_mask = torch.ones(1, tgt_len, src_len)
    
    # 将填充位置的掩码设为0
    for i in range(len(english_sentence), src_len):
        attention_mask[0, :, i] = 0
        
    print("\n情景2: 含填充的句子翻译 (使用填充掩码)")
    print(f"源语言 (含填充): {' '.join(padded_src_tokens)}")
    print(f"目标语言: {' '.join(tgt_tokens)}")
    print(f"注意力掩码:\n{attention_mask[0]}")
    
    # 计算带掩码的注意力
    _, masked_attention_weights = cross_attention(tgt_seq, padded_src_seq, padded_src_seq, attention_mask)
    
    # 可视化带掩码的注意力权重
    visualize_attention_weights(
        masked_attention_weights[0], 
        padded_src_tokens, 
        tgt_tokens, 
        "Translation Attention (With Mask)"
    )
    
    # 情景3: 模拟真实翻译过程中的仅限前向掩码
    print("\n情景3: 模拟自回归生成过程")
    print("在自回归解码时，我们逐个生成目标单词")
    
    # 假设目标序列是逐个生成的
    for i in range(1, len(tgt_tokens) + 1):
        current_tgt_tokens = tgt_tokens[:i]
        current_tgt_seq = torch.stack([tgt_embeddings[token] for token in current_tgt_tokens]).unsqueeze(0)
        
        _, step_attention_weights = cross_attention(current_tgt_seq, src_seq, src_seq)
        
        print(f"\n生成到 '{' '.join(current_tgt_tokens)}'")
        visualize_attention_weights(
            step_attention_weights[0], 
            src_tokens, 
            current_tgt_tokens, 
            f"Decoding Step {i}"
        )
    
    print("\n总结:")
    print("1. 交叉注意力使解码器能够关注与当前生成单词相关的源语言单词")
    print("2. 注意力掩码可以屏蔽填充标记，确保模型不关注无意义的位置")
    print("3. 在自回归生成过程中，每生成一个新单词都会基于之前生成的单词和源语言内容计算新的注意力权重")
    print("4. 注意力权重可以显示每个目标单词对源句子不同部分的依赖程度，提供可解释性")

if __name__ == "__main__":
    translation_example() 
