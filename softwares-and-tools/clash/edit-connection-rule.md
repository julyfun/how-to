---
title: edit-connection-rule
date: 2024-01-15 01:11:03
tags: ["softwares-and-tools", "clash"]
---
参见：

https://jichanggo.com/clash%E9%AB%98%E7%BA%A7%E8%BF%9B%E9%98%B6%E6%95%99%E7%A8%8B

Choose a profile (like `xxx.yaml`)

## Not stable method

Edit. In rules array, add:

```yaml
- DOMAIN-SUFFIX,openai.com,Proxy
```

表示后缀为 `openai.com` 的网站走代理

但是你编辑这个文件可能会被机场覆盖。

## 长期修改: Mixin

修改 Mixin 文件，例如在 clash for windows 里在 Settings -> Mixin -> YAML -> Edit 中，修改如下：

```yml
mixin: # object
  rules:
    - "DOMAIN-SUFFIX,openai.com,Proxy"
    - "DOMAIN-SUFFIX,bilibili.com,DIRECT"
```

记得开启 Mixin 模式，cfw 中在首页。

- 如果 yaml 一 Mixin 就炸（指全部走直连了）

那就用 js 文件吧。选择用 Javascript 而不是 yaml，然后写：

```js
module.exports.parse = async (
{ content, name, url },
{ yaml, axios, notify }
) => {
content.rules.unshift("DOMAIN-KEYWORD,wikimedia,Proxy");
return {...content};
};
```

