```
https://stackoverflow.com/questions/3796927/how-do-i-git-clone-a-repo-including-its-submodules
```

## Clone with submodules

```
git clone --recurse-submodules -j8 git://github.com/foo/bar.git
```

## Already cloned, get submodules

```
git submodule update --init --recursive
```

