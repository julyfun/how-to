---
reliability: "[20% (author), 0 / 0 (visitor)]"
date: 2024-07-10
language: "zh-hans"
os: "Linux DESKTOP-I44J4US 5.15.153.1-microsoft-standard-WSL2 #1 SMP Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
author: "Julyfun"
suppose-you-know: [computer]
keywords: []
---

# Add exisiting local git repo as submodule as a submodule to parent directory repo?

```
git submodule add ./Segmentation1 Segmentation1
# this is optional
git submodule absorbgitdirs Segmentation1
# add submodule's url
git config -f .gitmodules submodule.Segmentation1.url \
        https://github.com/etc/path.git
```

ref: https://www.reddit.com/r/git/comments/edn49q/how_to_add_existing_local_git_repo_as_a_submodule/

Verified on 24/7/10.

