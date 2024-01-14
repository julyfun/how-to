https://stackoverflow.com/questions/74624084/could-not-auto-determine-entry-point-from-rollupoptions

我把项目里所有 diff 给 stash 了，再重新 pop，结果居然没报这个问题了。报问题的时候似乎没有正确读取 3000 端口而是用了默认的 5173（尽管我在 vite.config.js 中已经指定了 3000）

## another solution

重启终端环境。

## another another solution

回到根目录进行 run dev.

