https://stackoverflow.com/questions/355907/how-do-i-repeat-an-edit-on-multiple-lines-in-vim

## 1

for the text:

```
abc123abc
def456def
ghi789ghi
```

you do:

```
Ctrl - v
jj # select 3 lines
Shift - I
, # insert a comma
Esc # at this moment, three commas gonna be added
```

you get:

```
abc,123abc
def,456def
ghi,789ghi
```

## 2

use `ctrl + v` to and move cursor, you'll select several lines, you can do operations in normal mode, for example `x` to delete a character.

