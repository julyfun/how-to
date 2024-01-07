```md
&&\begin{aligned}
& g_{t, i, k, j} \mathrel{{+}{=}} C_{t - l_i}^{j - k} * 2^{j - k} , \text{if } i = k \text{ and } a_t < B_i \\
& g_{t, i, k, j} \mathrel{{+}{=}} g_{t - 1, i + 1, k, j}, \text{if } i \neq k \text{ and } a_t = B_i \\
& g_{t, i, k, j} \mathrel{{+}{=}} f_{t - 1, i, j - 1}, \text{if } j = k \text{ and } a_t < B_j \\
& g_{t, i, k, j} \mathrel{{+}{=}} g_{t - 1, i, k, j - 1}, \text{if } j \neq k\\
\end{aligned}$$
```

