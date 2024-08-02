# Vscode cannot connect to remote Linux （_WebSocket close with status code 1006)

??? info "Problem environment"

    - author: Julyfun MacOS14.5 M1
    - edited date: 2024-08-02
    - expected environment: win10, wsl 

## Details of the problem / Steps to reproduce the error

_No details_

---

## Best practice

- ref: https://stackoverflow.com/questions/68799580/vscode-cannot-connect-to-remote-linux-websocket-close-with-status-code-1006

```
wsl --shutdown
wsl 
```

I've also closed the vscode window that are trying to reconnect wsl. (No need to close all vscode window)

> verified on 24.8.2

