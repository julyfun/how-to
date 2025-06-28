---
title: "npm-install-hangs-on-sill-idealtree-build"
date: 2024-01-15 01:10:05
tags: []
---
## Env

MacOS 13 M1

## Try

I tryed everything here, non solves, 

https://stackoverflow.com/questions/50522376/npm-install-hangs-on-loadidealtreeloadalldepsintoidealtree-sill-install-loadid

https://github.com/npm/cli/issues/4309

But suddenly `npm install` works again...

## Final State

I don't know which one works.

- IPV6 auto connection is enabled (just don't modify it)
- `package-lock.json` and `node_modules` are removed
- npm version is `system`, which is npm@10.2.3 and node@v21.2.0
- `alias npm="node --dns-result-order=ipv4first $(which npm)"`
- `npm set registry https://registry.npmjs.org`
- vpn rule: Rule

