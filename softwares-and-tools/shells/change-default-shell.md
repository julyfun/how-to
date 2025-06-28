---
title: "add result of (which fish) generally /usr/bin/fish"
date: 2024-03-14 10:19:00
tags: []
---
```
sudo vim /etc/shells
# add result of (which fish) generally /usr/bin/fish
chsh -s /usr/bin/fish # maybe sudo chsh
```

Restart your terminal and see if this works.

