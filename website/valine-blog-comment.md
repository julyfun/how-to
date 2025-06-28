---
leancloud 注册账号创建应用，把域名填入安全域名。
valine 提供的 js 放入 `<head>`
把 leancloud 上的 appid 和 appkey 放入 html body 中的
date: 2024-01-15 01:10:05
title: valine-blog-comment
tags: []
---

```html
          <div id="vcomments"></div>
          <script>
            new Valine({
              el: '#vcomments',
              appId: 'Jx6fTElQS3cweoHbEj8wyWLt-gzGzoHsz',
              appKey: '0LI9g0Hq8L8ShGBdxlnPZjdb'
            })
          </script>
```

- 调节它的位置和 css。
- new Valine 中加入 `meta: ['nick']` 可以只显示名字框。

