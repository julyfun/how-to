---
keywords: [workspace]
---

对于一个项目，你执行 python somewhere/main.py

则 main.py 运行的所有东西，包括 main.py import 的 py，其中的 import 的 sys.path（sys.path 会决定 import 的位置） 均为 somewhere/（即 main.py 所在的位置）。

> 例如 main.py 中 from pkg1.animal import eat, animal.py 有 from mantis import something，则 mantis 必须在 main.py 所在文件夹下，不可以在 pkg1/ 中。

但是 vscode 的智能提示比较呆，会从当前文件 __init__.py 的祖先文件夹都会自动加入智能提示的 sys.path.

## other solutions

你也可以 from .somedir import xxx

> [what] 这啥玩意

## sys.path.append 的作用范围？

```py
cur_dir = os.path.dirname(__file__)
print(cur_dir)
# Add the parent directory to the Python path
sys.path.append(cur_dir)
print(sys.path, type(sys.path))
```

该语句后所有的 import （就算 import 文件中的 import 也可以）都会用这个新的 path.

## 注意 import 后不再能文件夹寻址

如果有 plant/apple/eat.py

你可以 import plant.apple.eat.some

但不可以 import plant 之后再 a = plant.apple.eat.some()

