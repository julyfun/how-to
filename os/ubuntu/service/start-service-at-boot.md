查看如下教程，注意，需要 sudo su nvidia -c 'bash /home/nvidia/Workspace/autoaim_startup.sh' 以用 nvidia 环境：

tested ref: https://www.linode.com/docs/guides/start-service-at-boot/

- Tested in 2023, on Nvidia AGX. No problem.

## Sol 2

```
sudo nano /etc/systemd/system/my_script.service
```

```
[Unit]
Description=My Custom Script
After=network.target

[Service]
Type=simple
ExecStart=/path/to/your/script.sh
Restart=on-failure
User=your_username  # 可选，指定运行用户（如 root 或普通用户）

[Install]
WantedBy=multi-user.target
```

```
chmod +x /path/to/your/script.sh
```

```
sudo systemctl daemon-reload         # 重新加载 systemd 配置
sudo systemctl enable my_script      # 开机自启动
sudo systemctl start my_script       # 立即运行
```

```
sudo systemctl status my_script
```

