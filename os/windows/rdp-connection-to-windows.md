Using the RDP protocol, connect to windows desktop from Ubuntu.

```
sudo apt install rdesktop
rdesktop -f -a 16 100.100.100.187:3389
```

You can try `telnet` command before connecting. `3389` is mostly the port for RDP.

```
telnet 100.100.100.187 3389
```

