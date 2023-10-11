> string length 'hello, world'
12

set str foo
> string length -q $str; echo $status
0
# Equivalent to test -n "$str"

> string length --visible (set_color red)foobar
# the set_color is discounted, so this is the width of "foobar"
6

> string length --visible 🐟🐟🐟🐟
# depending on $fish_emoji_width, this is either 4 or 8
# in new terminals it should be
8

> string length --visible abcdef\r123
# this displays as "123def", so the width is 6
6

> string length --visible a\nbc
# counts "a" and "bc" as separate lines, so it prints width for each
1
2

