---
title: multi-user
date: 2024-09-02 15:20:56
tags: ["GitHub"]
---
*This multi-user means mutli github users in one machine.*
 
ssh-keygen another key with another password (can be empty).

name it id_rsa_julyfun

add it to your github account ssh key. 

ref: https://stackoverflow.com/questions/4220416/can-i-specify-multiple-users-for-myself-in-gitconfig

in your ~/.ssh/config, add

```yml
Host github-julyfun
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_julyfun
```

## test

ssh -T git@github-julyfun

## Usage

```
git remote set-url origin git@github-julyfun:foo/bar.git
git clone git@github-julyfun:ArnaudRinquin/atom-zentabs.git
```

