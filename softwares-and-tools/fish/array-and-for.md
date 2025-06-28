---
title: array-and-for
date: 2024-01-16 21:21:18
tags: []
---
https://stackoverflow.com/questions/50027770/fish-shell-how-to-append-an-element-to-an-array

set -l array "tiny tim" bob
set -l children joe elias matt

echo $children
for i in (seq 2)
    set children (string join " " $children $array[$i])
end
echo $children

