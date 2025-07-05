---
title: How to override heading numbering behavior in Typst
date: 2024-10-10 15:41:38
tags: ["langs", "typst"]
---
# How to override heading numbering behavior in Typst

ref: https://stackoverflow.com/questions/78110939/how-to-override-heading-numbering-behavior-in-typst 

```typst
#set heading(numbering: (..numbers) => {
  let level = numbers.pos().len()
  if (level == 1) {
    return numbering("I", numbers.pos().at(level - 1))
  } else if (level == 2) {
    return numbering("A", numbers.pos().at(level - 1))
  } else {
    return numbering("1", numbers.pos().at(level - 1))
  }
})
```

