---
reliability: '[20% (author), 0 / 0 (visitor)]'
language: Chinese
os: 'Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1
  20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64'
author: Julyfun MacOS14.5 M1
suppose-you-know:
- computer
date: 2024-05-21
title: click all invite
tags: ["website", "zhihu"]
---
# click all invite

```js
// 获取所有按钮
const allButtons = document.getElementsByTagName('button');

// 遍历所有按钮
for (let i = 0; i < allButtons.length; i++) {
  // 检查按钮文本是否包含 '邀请回答'
  if (allButtons[i].textContent.includes('邀请回答')) {
    // 模拟点击事件
    allButtons[i].click();
  }
}
```

