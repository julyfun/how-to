---
reliability: "[50% (author), 0 / 0 (visitor)]"
date: 2024-05-14
language: "Chinese"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
author: "Julyfun MacOS13.4 M1"
suppose-you-know: [computer]
keywords: [快速操作，服务，终端]
---

os: mac14.5

# create a quick action to open folder in terminal

创建快速操作以右键在终端中打开文件夹

- 打开 Automator app，又称自动操作
- 新建文件
- 在“选取文稿类型”窗口中选择“快速操作”，点击“选取”
- 在左侧栏目中拖拽“实用工具 - 运行 Apple Script”到右侧空白处
- 在顶部栏目中选择“工作流程接收到 自动（无）” “位于 访达.app”
- 添加以下脚本：

```applescript
on run {input, parameters}
	tell application "Finder"
		set currentFolder to (folder of the front window as alias)
	end tell
	tell application "iTerm"
		activate
		try
			set currentSession to current session of current window
		on error
			create window with default profile
			set currentSession to current session of current window
		end try
		tell currentSession
			write text "cd " & quoted form of POSIX path of currentFolder
		end tell
	end tell
	return input
end run
```

- 保存取个名字
- `killall Finder` 重启 Finder 后，右键一个文件夹，在“快速操作”栏目中寻找是否有对应服务。

## Optional

- 在设置 - 键盘 - 键盘快捷键 - 服务 - 通用 中为你的服务增加快捷键，（双击快捷键图标后键入新快捷键）比如 `cmd + ;`

