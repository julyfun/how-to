## 分为学生评教和过程评教

这两个评教页面的框架还不同，无语。

### 1.

```js
var option_btn = document.getElementsByClassName("radio-pjf");
for (var j = 0; j < option_btn.length; j += 5) { option_btn[j].click(); }
var txt = document.getElementsByClassName("form-control input-zgpj");
txt[0].value = "减少作业量"; txt[1].value = "减少作业量";
window.scrollTo(0, 10000);
```

对于每个课程，复制到浏览器 F12 中的 Console 即可，需要手动点击提交，因为网页会检测是否是脚本点击的提交。

浏览器可能会拒绝你复制。此时你需要输入 `allow pasting`.

### 2.

```js
var mui = document.querySelectorAll('li.mui-table-view-cell.li-0715E896D64DBEBEE065F8163EE1DCCC')
mui[0].querySelector('div.item-2 > div.mui-clearfix > div.block:nth-of-type(5)').click()
mui[1].querySelector('div.item-2 > div.mui-clearfix > div.block:nth-of-type(1)').click()
var textareas = document.querySelectorAll('textarea');
textareas.forEach(function(textarea) {
    textarea.value = '加快作业批改，作业均匀设置，可以每课后一个小作业';
    textarea.click();
});
textareas[0].click();
```

每学期的过程评价的 class 稍有不同，需检查网页源码中 mui-table-view-cell 元素下的 class (以 `li-` 开头）。例如，可能需要将上述代码的第一行改为：

```
var mui = document.querySelectorAll('li.mui-table-view-cell.li-11B257C0903EB5F4E065F8163EE1DCCC')
```

对于每个课程复制到 Console，注意不知道网页检测了什么的缘故，必须要三个文本框都点击一下他才允许提交。

