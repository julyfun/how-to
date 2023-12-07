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
    - "DOMAIN-SUFFIX,bilibili.com,Direct"
```

