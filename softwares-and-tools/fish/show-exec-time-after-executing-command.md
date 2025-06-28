---
reliability: [60% (author), 0 / 0 (visitor)]
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:53:44 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
date: 2024-05-07
title: "Show exec time after executing command"
---

# Show exec time after executing command

ref: https://www.reddit.com/r/fishshell/comments/4yyoi5/see_the_time_of_execution_after_the_end_of_a/

```
function printtime --on-event fish_postexec
        set duration (echo "$CMD_DURATION 1000" | awk '{printf "%.3fs", $1 / $2}')
        echo \t\($duration\)
end
```

