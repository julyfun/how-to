---
title: batch-rename-file-extension-in-a-for-loop
date: 2024-01-16 21:21:18
tags: []
---
Thanks to `basename`, which is a unix bin file

https://stackoverflow.com/questions/38590165/how-to-rename-file-extentions-in-fish-in-a-for-loop

```
for file in *.md
    mv -v -- "$file" (basename $file .md).txt 
end
```

use string replace is also nice.

