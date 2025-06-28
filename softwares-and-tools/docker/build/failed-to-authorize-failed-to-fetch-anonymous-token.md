---
title: "failed-to-authorize-failed-to-fetch-anonymous-token"
date: 2024-04-03 14:32:19
tags: []
---
```
 => ERROR [internal] load metadata for docker.io/library/python:3.10-slim-bullseye                                                                                                       10.0s
------
 > [internal] load metadata for docker.io/library/python:3.10-slim-bullseye:
------
Dockerfile:1
--------------------
   1 | >>> FROM python:3.10-slim-bullseye
   2 |     WORKDIR /opt/app
   3 |     ENV PYTHONPATH "${PYTHONPATH}:/opt/app"
--------------------
ERROR: failed to solve: python:3.10-slim-bullseye: failed to authorize: failed to fetch anonymous token: Get "https://auth.docker.io/token?scope=repository%3Alibrary%2Fpython%3Apull&service=registry.docker.io": net/http: TLS handshake timeout
make: *** [Makefile:21: build.docker] Error 
```

## Sol

Just retry.

