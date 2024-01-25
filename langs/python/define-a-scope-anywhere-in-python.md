---
keywords: [temporary scope]
---

ref: https://stackoverflow.com/questions/8046142/can-i-define-a-scope-anywhere-in-python

## NO

Substitution:

```
def f():
    ...
f()
```

```
try:
    a = 1
    b = 2
finally:
    del a
    del b
```

