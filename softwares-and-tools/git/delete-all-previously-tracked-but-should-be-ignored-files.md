https://stackoverflow.com/questions/1274057/how-do-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore?page=1&tab=scoredesc#tab-top

no better way but:

```
git rm -r --cached .
git add .
```

