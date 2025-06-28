---
title: setup-on-new-pc-with-existing-planet
date: 2025-06-18 21:28:03
tags: []
---
## Linux

- sudo snap install zerotier
- download planet
- replace `/var/lib/zerotier-one/planet`
- [Not needed during test] sudo service zerotier-one restart
- sudo zerotier-cli join <id>
- Remote ui approve this.
- See zerotier-cli peers

