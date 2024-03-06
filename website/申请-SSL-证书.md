---
platform: 阿里云
service: nginx
---

每隔一年这玩意就会过期。

首先打开数字证书管理服务（阿里云），

https://yundun.console.aliyun.com/?spm=5176.7968328.J_8413632810.4.177865c3sxu2Yy&p=cas#/certExtend/free/cn-hangzhou

- 点击 SSL 证书 - 免费证书 - 立即购买。
- 购买一个免费或者付费证书。
- 购买后不会直接显示在免费证书栏目里，需要创建证书。
- 创建证书时填写 www.mfans.fans 其他好像没什么要填写的
- 很快就会审核通过，通过后在免费证书栏目里会出现这个证书。
- 点击证书右边的下载。下载 nginx 版本。
- 得到 zip 解压得到 .key 和 `.pem`
- 把这两个文件拷贝到服务器的 `/etc/nginx/cert`
- 在 /etc/nginx 下 `grep -nr key` 看看哪个文件在引用 key 和 pem，可能是 /etc/nginx/sites-available/default 文件，把他引用的 key 改成新的
- `sudo systemctl restart nginx`
- 好了

