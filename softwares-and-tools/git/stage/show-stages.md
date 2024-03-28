ref: https://stackoverflow.com/questions/1587846/how-do-i-show-the-changes-which-have-been-staged

```
git diff --cached # show staged
git diff --name-only --cached # show files only

git diff # show unstaged
git diff HEAD # show staged and unstaged (till last commit)
```

