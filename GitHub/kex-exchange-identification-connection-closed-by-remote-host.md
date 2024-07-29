# kex_exchange_identification: Connection closed by remote host

??? info "Problem environment"

    - expected environment: unix

## Details of the problem / Steps to reproduce the error

Some time when you try to connect to github, you may get this error:

```
kex_exchange_identification: Connection closed by remote host
```

---

# Answer 1

??? info "Answer environment"

    - author: julyfun@github
    - verified date: 24-7-29
    - verified environment: As in the problem

- ref: no

## TLDR

Add this to your `~/.ssh/config`:

```
Host github.com
  Hostname 20.200.245.248
  Port 443
```

## What I've done before the problem is solved (don't know which one worked):

- Close clash for windows
- cancel `http_proxy` and other proxy ports in shell config file (config.fish) and `~/.gitconfig`
- delete all content in `~/.ssh/known_hosts`
- ref: `https://github.com/orgs/community/discussions/55269`, use `ssh -Tv -p 443 git@ssh.github.com`, or add this to `~/.ssh/config`:

```
Host github.com
  Hostname 20.200.245.248
  Port 443
```

> verified on 24/5/28, for a new user on Ubuntu, adding this content to `config` is useful.
> verified on 24/7/24, worked for wsl when suddenly can't connect git by cli.

## Post test

- reopen clash for windows: still ok to ssh
- git clone: ok
- git pull and push: ok
