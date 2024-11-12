- reliability: "20% (author)"
- date: 2024-11-12
- os: "Win 11"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# Setup ssh server on win

- https://blog.csdn.net/weixin_72910567/article/details/132414264
- Verified on 24.11.12, win11, ok, will attach Cmd not Powershell

- Need passwordless?
    - upload client `id_rsa.pub` to server's `~/.ssh/authorized_keys`
    - Edit `C:\ProgramData\ssh\sshd_config`
        - set `PubkeyAuthentication yes`
        - comment this `AuthorizedKeysFile..`: (ref: https://superuser.com/questions/1698831/ssh-into-a-passwordless-windows-10-pc)
        ```
        Match Group administrators
        # AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
        ```
    - ok on 24.11.12

