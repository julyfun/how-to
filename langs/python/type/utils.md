---
title: "Python Type Utils"
date: 2025-06-24 14:36:22
tags: [python, python-type]
---

## Inheritance tree

[tested-ok-and-copy-here]

```python
def print_inheritance_tree(cls, indent='', last=True, is_root=True):
    if is_root:
        print(cls.__name__)
    else:
        connector = '└── ' if last else '├── '
        print(indent + connector + cls.__name__)
        indent += '    ' if last else '│   '
    bases = cls.__bases__
    for i, base in enumerate(bases):
        is_last = i == (len(bases) - 1)
        print_inheritance_tree(base, indent, is_last, is_root=False)
```
