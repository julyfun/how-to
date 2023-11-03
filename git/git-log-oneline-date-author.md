https://stackoverflow.com/questions/1441010/the-shortest-possible-output-from-git-log-containing-author-and-date

```
git log --pretty="%C(Yellow)%h  %C(reset)%ad (%C(Green)%cr%C(reset))%x09 %C(Cyan)%an: %C(reset)%s" --date=short -7
```

