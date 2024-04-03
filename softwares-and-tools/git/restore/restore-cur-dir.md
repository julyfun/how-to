ref: https://stackoverflow.com/questions/15404535/how-to-git-reset-hard-a-subdirectory

```
git restore --source=HEAD --staged --worktree -- .
git restore -s@ -SW -- <path>
```

