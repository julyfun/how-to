---
title: "rdp-connection-to-windows"
date: 2024-03-06 18:37:15
tags: []
---
Using the RDP protocol, connect to windows desktop from Ubuntu.

Once you type the following command, you will enter full screen mode to windows desktop instantly. RDP shall be set on windows before connecting.

```
sudo apt install rdesktop
rdesktop -f -a 16 100.100.100.187:3389
```

You can try `telnet` command before connecting. `3389` is mostly the port for RDP.

```
telnet 100.100.100.187 3389
```

Use ctrl + alt + enter to quit full screen.

