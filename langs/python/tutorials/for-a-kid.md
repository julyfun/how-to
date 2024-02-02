---
reliability: 20%
suppose-you-know: python 输入输出
---

## 函数 `def func():`

### 语法

```py
def func(r): # 函数名为 func，这是自定义的
    PI = 3.1415926
    return r * PI * PI # 函数需要一个返回值，用 return
```

函数可以被多次利用，就像 `len()` 函数用来求列表长度一样。

### 例题 1

* 写一个函数，求半径为 `r` 的圆的面积。

```py
def S(r): # 求半径为 r 的圆的面积
    PI = 3.1415926
    return r * PI * PI
print(S(5)) # 输出 49.3480203218738
```

### 例题 2

* 判断一个整数是否是偶数，如果是，返回 `True`。

```py
def even(n):
    if n % 2 == 0:
        return True
    return False # 可以按条件写多条 return 语句
```

## 集合 `set()`

### 语法

集合可以用来存数据。它和 `list` 相似，不同的是 `set` 中数据自动排序，而且不会重复出现。

```py
s = set()
s.add(1)
s.add(1)
s.add(2)
print(s)
# 输出为 {1, 2}
s.remove(1)
print(s)
# 输出为 {2}
```

