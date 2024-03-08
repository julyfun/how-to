#set page(paper: "us-letter")
#set heading(numbering: "1.1")

// 这是注释
#figure(image("sjtu.png", width: 50%)) \ \ \

#align(center, text(17pt)[
  #set block(spacing: 2em)
  *Laboratory Report of Digital Signal Processing* \ \
  Name: Junjie Fang \ \
  Student ID: 521260910018 \ \
  Date: 2024/3/4 \ \
  Score: #h(4em)
])

#pagebreak()

#set page(header: align(right)[
  Laboratory Report of Digital Signal Processing - Junjie FANG
], numbering: "1")
#set text(size: 11pt)

#outline()

= Data sampling and reconstruction

== Question 1

Given the parameters $A = 3, B = 4, D = 8$, the three gate functions are defined
by:

$
  g_0(t) &:= cases(4 "if" 0 <= t <= 3, 0 "otherwise") \
  g_1(t) &:= cases(4 "if" -3 / 8 <= t <= -3 / 5 \
  0 "otherwise") \
  g_2(t) &:= cases(8 "if" 8 <= t <= 11 \
  0 "otherwise")
$

And we know:

$
  x(t) := sum_(i = 0)^2 g_i (t)
$

We plot the $x$ function in the figure below:


It can be seen that the images of the three gate functions do not overlap.

In practice, we use python's `matplotlib` to draw function images. For
scalability, we use the `gate_func()`, `func_transform()` and
`add_func()` to generate, transform and add functions.

== Question 2

Let the frequencies corresponding to the two peaks in the image be $f_(a 1), f_(a 2)$ and
the function values be $X_1, X_2$. The sampling frequency is $f_s = 100"Hz"$.
According to the sampling theorem, we have:

$
  f_(a 1) &= plus.minus f_1 - k_1 f_s\
  f_(a 2) &= plus.minus f_2 - k_2 f_s\
$

where:

$
  k_1, k_2 != 0 \
  800"Hz" <= f_1, f_2 <= 850"Hz"
$

Plug the data $f_(a 1) = 14, f_(a 2) = 3$ into the equation and we can determine
that the only solution is:

$
  k_1 = 8, f_1 = 814"Hz" \
  k_2 = 8, f_2 = 803"Hz"
$

Next, we can determine the amplitudes $A_1$ and $A_2$ by reviewing some of the
properties of _Contiunous-Time Fourier Transform (CTFT)_. The Fourier Transform 
used in this question is in the form:

$
  X(j f) &= integral_(-oo)^(+oo) x(t) e^(-j 2 pi f t) dif t \
  x(t) &= integral_(-oo)^(+oo) X(j f) e^(j 2 pi f t) dif f
$

In this form, the cosine wave with amplitude $1$ and the following sum of two
impulse function form a Fourier Transform pair:

$
  cos(2 pi f_0 t) & <==>^("F.T.") 1 / 2 (delta(f - f_0) + delta(f + f_0)) \
$

Due to the linearity of Fourier Transform, we know that the amplitudes should be
twice the height of peaks in the frequency domain. Therefore, we have:

$
  A_1 = 2 X_1 = 4 \
  A_2 = 2 X_2 = 2
$

#align(center,
  table(
    columns: (auto, auto, auto),
    inset: 10pt,
    align: center,
    [Parameters], [$i = 1$], [$i = 2$],
    $f_i$, [$814"Hz"$], [$803"Hz"$],
    $A_i$, [4], [2]
  )
)

= Appendix Code

The following python code is used to plot the function graph of Question 1.

#import "@preview/codelst:1.0.0": sourcecode

#sourcecode[
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate a gate function with the given parameter
def gate_func(A, B):
    def output_func(t):
        return np.where((t >= 0) & (t <= A), B, 0)
    return output_func

# Transform a function. Parameter shifting is given by param_func(), and the value is multiplied by `times`
def func_transform(func, param_func, times):
    def output_func(x):
        return func(param_func(x)) * times
    return output_func

# Returns with a function whose output is the sum of the outputs of f and g
def add_func(f, g):
    def output_func(x):
        return f(x) + g(x)
    return output_func 
    

A = 3
B = 4
D = 8

g0 = gate_func(A, B)
g1 = func_transform(g0, lambda t: 3 * t + D, 1)
g2 = func_transform(g0, lambda t: t - D, 2)

x_func = add_func(add_func(g0, g1), g2)

x_values = np.linspace(-5, 12, 1000)
y_values = x_func(x_values)
plt.plot(x_values, y_values, label=f'x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()
```
]

