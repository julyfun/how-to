ref: https://stackoverflow.com/questions/38623138/how-to-set-the-working-directory-for-debugging-a-python-program-in-vs-code

In launch.json, specify a dynamic working directory (i.e. the directory where the currently-open Python file is located) using:

```
"cwd": "${fileDirname}"
```

