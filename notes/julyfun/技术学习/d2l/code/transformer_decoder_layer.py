import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    """
    多头注意力机制
    """
    def __init__(self, d_model, n_heads, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        
        # 线性投影层
        self.query_proj = nn.Linear(d_model, d_model)
        self.key_proj = nn.Linear(d_model, d_model)
        self.value_proj = nn.Linear(d_model, d_model)
        self.output_proj = nn.Linear(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)
        
    def split_heads(self, x, batch_size):
        x = x.view(batch_size, -1, self.n_heads, self.d_k)
        return x.transpose(1, 2)
        
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        
        # 线性投影
        query = self.query_proj(query)
        key = self.key_proj(key)
        value = self.value_proj(value)
        
        # 分割头
        query = self.split_heads(query, batch_size)
        key = self.split_heads(key, batch_size)
        value = self.split_heads(value, batch_size)
        
        # 缩放点积注意力
        scores = torch.matmul(query, key.transpose(-2, -1))
        scores = scores / torch.sqrt(torch.tensor(self.d_k, dtype=torch.float32))
        
        if mask is not None:
            # 处理掩码维度
            if mask.dim() == 3:
                mask = mask.unsqueeze(1)
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attention_weights = F.softmax(scores, dim=-1)
        attention_weights = self.dropout(attention_weights)
        
        context = torch.matmul(attention_weights, value)
        context = context.transpose(1, 2).reshape(batch_size, -1, self.d_model)
        output = self.output_proj(context)
        
        return output, attention_weights

class PositionwiseFeedForward(nn.Module):
    """
    位置前馈网络
    """
    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

class TransformerDecoderLayer(nn.Module):
    """
    Transformer 解码器层，包含:
    1. 自注意力机制（带序列掩码）
    2. 交叉注意力机制（连接编码器输出）
    3. 前馈网络
    """
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super(TransformerDecoderLayer, self).__init__()
        
        # 自注意力层
        self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
        # 交叉注意力层
        self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)
        # 前馈网络
        self.feed_forward = PositionwiseFeedForward(d_model, d_ff, dropout)
        
        # 层标准化
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, encoder_output, self_attn_mask=None, cross_attn_mask=None):
        """
        Args:
            x: 解码器输入 (batch_size, tgt_len, d_model)
            encoder_output: 编码器输出 (batch_size, src_len, d_model)
            self_attn_mask: 自注意力掩码 (batch_size, tgt_len, tgt_len)
            cross_attn_mask: 交叉注意力掩码 (batch_size, tgt_len, src_len)
        """
        # 1. 自注意力子层 (带残差连接和层标准化)
        attn_output, self_attn_weights = self.self_attn(x, x, x, self_attn_mask)
        x = self.norm1(x + self.dropout(attn_output))
        
        # 2. 交叉注意力子层 (带残差连接和层标准化)
        # 这里是真正的交叉注意力 - query来自前一层，key和value来自编码器输出
        cross_attn_output, cross_attn_weights = self.cross_attn(
            query=x,
            key=encoder_output, 
            value=encoder_output, 
            mask=cross_attn_mask
        )
        x = self.norm2(x + self.dropout(cross_attn_output))
        
        # 3. 前馈网络子层 (带残差连接和层标准化)
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))
        
        return x, self_attn_weights, cross_attn_weights

# 演示代码
def decoder_layer_demo():
    """
    演示 Transformer 解码器层中交叉注意力的使用
    """
    # 设置随机种子
    torch.manual_seed(42)
    
    # 模型参数
    batch_size = 2
    src_len = 7    # 源序列长度（编码器输入）
    tgt_len = 5    # 目标序列长度（解码器输入）
    d_model = 64   # 模型维度
    n_heads = 8    # 多头数量
    d_ff = 256     # 前馈网络维度
    
    # 创建解码器层
    decoder_layer = TransformerDecoderLayer(d_model, n_heads, d_ff)
    
    # 模拟输入
    # 解码器输入
    decoder_input = torch.randn(batch_size, tgt_len, d_model)  
    # 编码器输出
    encoder_output = torch.randn(batch_size, src_len, d_model)
    
    # 创建掩码
    # 1. 自注意力掩码（未来信息掩码，下三角矩阵）
    self_attn_mask = torch.ones(batch_size, tgt_len, tgt_len)
    # 创建下三角矩阵掩码
    for i in range(tgt_len):
        for j in range(tgt_len):
            if j > i:  # 当 j > i 时，也就是位置在右上方（代表未来位置）
                self_attn_mask[:, i, j] = 0
    
    # 2. 交叉注意力掩码（模拟源序列填充掩码）
    cross_attn_mask = torch.ones(batch_size, tgt_len, src_len)
    cross_attn_mask[:, :, -2:] = 0  # 假设最后两个源位置是填充的
    
    # 前向传播
    output, self_attn_weights, cross_attn_weights = decoder_layer(
        decoder_input, encoder_output, self_attn_mask, cross_attn_mask
    )
    
    # 打印结果
    print("==== Transformer 解码器层演示 ====")
    print("\n输入形状:")
    print(f"  解码器输入: {decoder_input.shape}")
    print(f"  编码器输出: {encoder_output.shape}")
    print(f"  自注意力掩码: {self_attn_mask.shape}")
    print(f"  交叉注意力掩码: {cross_attn_mask.shape}")
    
    print("\n掩码可视化:")
    print("  自注意力掩码 (未来信息掩码):")
    print(self_attn_mask[0])
    print("\n  交叉注意力掩码 (源序列填充掩码):")
    print(cross_attn_mask[0])
    
    print("\n输出形状:")
    print(f"  解码器层输出: {output.shape}")
    print(f"  自注意力权重: {self_attn_weights.shape}")
    print(f"  交叉注意力权重: {cross_attn_weights.shape}")
    
    # 分析注意力权重
    print("\n分析交叉注意力权重:")
    # 选择第一个样本的第一个头
    head_idx = 0
    sample_idx = 0
    
    print(f"第{sample_idx+1}个样本、第{head_idx+1}个头的交叉注意力权重:")
    print(cross_attn_weights[sample_idx, head_idx])
    
    # 验证交叉注意力掩码的效果
    print("\n验证交叉注意力掩码效果:")
    mask_effect = cross_attn_weights[sample_idx, head_idx] * cross_attn_mask[sample_idx]
    print("掩码后的权重 (被掩码的位置应为0):")
    print(mask_effect)
    
    # 总结交叉注意力的作用
    print("\n总结:")
    print("1. 交叉注意力允许解码器关注编码器的输出")
    print("2. 解码器的每个位置都可以通过交叉注意力访问编码器的全部信息")
    print("3. 交叉注意力掩码允许我们忽略编码器输出中的某些位置（如填充位置）")

if __name__ == "__main__":
    decoder_layer_demo() 
