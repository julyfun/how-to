这里 $x_i^->$ 表示一个方向的单位向量

## nabla

可当做一个向量看待

$$limits(nabla)^-> eq.def sum_i x_i^-> diff / (diff x_i) $$

## 梯度

$$"grad"(f) eq.def limits(nabla)^-> f = sum_i x_i^-> (diff f) / (diff x_i)$$

- 输入 $f$: $RR^n -> R$ 标量场，输出向量场. 
- $nabla f$ 对于一个向量输入，输出一个向量

## 散度

$$"div"limits(F)^-> eq.def limits(nabla)^-> dot limits(F)^-> = sum_i (diff F_x_i) / (diff x_i) $$
- 输入向量场，输出标量场

## 旋度

$$"curl" limits(F)^-> eq.def nabla times limits(F)^->$$

## Laplace

$$laplace eq.def sum_i (diff ^ 2) / (diff x_i^2)$$

- 输入标量场，输出标量场（先做梯度运算，再做散度运算）
