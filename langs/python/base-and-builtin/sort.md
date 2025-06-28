---
title: 按自定义函数排序
date: 2024-02-02 23:48:19
tags: []
---
ref: https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/

```
a = [2, 1, 3]
b = sorted(a) # 不改变 a
a.sort() # 改变 a
a.sort(reverse=True)

# 按自定义函数排序
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

