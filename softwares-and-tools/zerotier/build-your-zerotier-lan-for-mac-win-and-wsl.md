- reliability: "20% (author)"
- date: 2024-10-29
- os: "macos 14.5, wsl2 ubuntu 22.04 in win11, win11"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# Build your zerotier LAN for mac, win and wsl

- Basic tutorial : https://github.com/xubiaolin/docker-zerotier-planet
    - `200 Join OK` on windows but windows is not listed in webui?
        - Double check the Port you selected when `./deploy.sh` is allows in your server security group!
        - Make sure you've `Easy Setup` the ip range (like in tutorial) (I make the IP range look like SJTU ethernet)

- For wsl2, if `zerotier join` completely failed and show `cannot bind to local control interface port 9993` in zerotier-one's log:
    - Make sure this in `wslconfig`, this is necessary:

```
[boot]
systemd=true
```

## Problems

- Can't ping wsl2 though webui show all devices are ONLINE?
    - Try pinging from each other (win, wsl, mac)
    - Do nothing and wait.
    - Done!

