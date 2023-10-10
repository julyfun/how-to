https://stackoverflow.com/questions/355907/how-do-i-repeat-an-edit-on-multiple-lines-in-vim

for the text:

```
abc123abc
def456def
ghi789ghi
```

you do:

```
Ctrl - v
jj
Shift - I
,
Esc
```

you get:

```
abc,123abc
def,456def
ghi,789ghi
```

