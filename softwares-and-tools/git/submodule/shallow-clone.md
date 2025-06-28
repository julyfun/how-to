---
title: "First time shallow clone (Or you can mofify .gitmodules manually instead of this command)"
date: 2024-07-28 21:45:19
tags: []
---
ref: https://stackoverflow.com/questions/2144406/how-to-make-shallow-git-submodules


```
# First time shallow clone (Or you can mofify .gitmodules manually instead of this command)
git submodule add --depth 1 git@github.com:lorem/ipsum.git path/to/submodule

# set permanently to shallow clone (like for deploying)
git config -f .gitmodules submodule.path/to/submodule.shallow true
```

