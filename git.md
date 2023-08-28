## 第一次上传
```
git push -u origin main
```

`-u`: This option, short for `--set-upstream`, tells Git to set up a tracking branch. It associates the remote branch with the local branch you are pushing. By using this option, you can use the simpler command git push in the future without specifying the remote and branch names every time.

## set default editor
```
git config --global core.editor "nvim"
```

## git 和远端分支比较

git diff main origin/main

## 删除远端分支

在网页端删除比较好。

```
git push origin --delete repo
git push origin :repo
```

## Rename a repo

在网页端 settings.

然后

```
git remote set-url origin git@github.com:someuser/newprojectname.git
```

