---
reliability: 20%
suppose-you-know: python 输入输出
date: 2024-02-05 01:37:59
title: 输出为 {1, 2}，已经自动排序
tags: []
---

## 1. 函数 `def func():`

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

## 2. 集合 `set()`

### 语法

集合可以用来存数据。它和 `list` 相似，不同的是 `set` 中数据自动排序，而且不会重复出现。

```py
s = set()
s.add(2)
s.add(2) # 添加元素，但如果已存在就什么都不做
s.add(1)
print(s)
# 输出为 {1, 2}，已经自动排序

s.remove(1) # 删除元素，如果元素不存在，则会发生错误
print(s)
# 输出为 {2}

s.clear() # 清空元素

print(2 in s) # 判断元素是否在集合中存在，输出为 False
```

你还可以这样创建一个 `set`：

```py
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# 输出为 {'orange', 'banana', 'pear', 'apple'}
```

> 注意：`basket = {}` 这种写法创建的是一个空的字典，不是一个空的集合。创建空集合应该使用 `basket = set()`。

### 例题 1

* 输入 $n$ 个数，去掉其中重复的数并从小到大输出，最后输出去重后还剩几个数。

```
n = int(input())
s = set(map(int, input().split())) # 将读入的一行数转换为 set
print(*s) # 输出 s 中的所有数字
print(len(s))
```

### 详细介绍

https://www.runoob.com/python3/python3-set.html

## 3. 字典 `dict()`

![](https://www.runoob.com/wp-content/uploads/2016/04/py-dict-3.png)

### 语法

```py
# 创建字典
d1 = { 'abc': 456 }
d2 = { 'abc': 123, 98.6: 37 }

# 获取字典中对应 key 的值
print(d1['abc']) # 456
print(d2[98.6]) # 37

# 修改字典
d1['abc'] = 123
print(d1['abc']) # 123

# 删除字典元素
del d1['abc'] # 删除一个键
d2.clear() # 清空字典
```

### 例题 1

https://blog.csdn.net/wc19862274581/article/details/124285529

**问题描述：**

输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。

**输入形式：**

一个字符串。

**输出形式：**

出现次数最多的字母以及其出现次数。

**样例输入：**

```
abcccd
```

**样例输出：**

```
c 3
```

**代码实现：**

```py
s = input()
ma = {}
for c in s:
    if c not in ma:  # 如果这个字母没有出现过就初始化为 1
        ma[c] = 1
    else:  # 否则加 1
        ma[c] += 1

ans = max(ma.values())  # ma.values() 获取所有的值
# items() 获取所有的键值对，用 sorted() 进行排序后重新用 dict() 重新组成一个有序字典 。这种排序是优先按键排序，其次按值排序
ma = dict(sorted(ma.items()))
for c, cnt in ma.items():
    if cnt == ans:
        print(c, cnt)
```

## 4. 排序 `.sort()` `sorted()`

ref: https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/

```
a = [2, 1, 3]
b = sorted(a) # 不改变 a
a.sort() # 改变 a
a.sort(reverse=True)

# 按特定函数排序
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]
programming_languages.sort(key=len)
programming_languages.sort(key=len, reverse=True)

# 按自定义函数排序
programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)
programming_languages.sort(key=get_year, reverse=True)
```

