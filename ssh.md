## ssh-keys

in ~/.ssh/config:

```
Host docker2
    HostName 172.17.0.2
    User nvidia
```

```
ssh-copy-id docker2
```

输入一次密码，然后后面就不用密码了。

