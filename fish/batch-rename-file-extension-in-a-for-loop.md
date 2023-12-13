Thanks to `basename`, which is a unix bin file

https://stackoverflow.com/questions/38590165/how-to-rename-file-extentions-in-fish-in-a-for-loop

```
for file in *.md
    mv -v -- "$file" (basename $file .md).txt 
end
```

use string replace is also nice.

