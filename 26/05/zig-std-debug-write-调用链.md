---
title: "zig std.debug.write 调用链"
date: 2026-05-28 17:59:36
tags: ["26", "05"]
author: "julyfun.m5air"
os: "Darwin julyfundeMacBook-Air.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:42 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8142 arm64"
assume-you-know: [computer]
confidence: 2
---

```
std.debug.print()
├── std.debug.lockStderr()
│   ├── Io.lockStderr()
│   │   ├── Threaded.lockStderr()
│   │   Threaded.initLockedStderr()
│   Io.LockedStderr.clear()
├── Io.Writer.print()
│   ├── Io.Writer.writeAll()
│   │   Io.Writer.write()
│   Io.Writer.printValue()
│   Io.Writer.writeAll()
std.debug.unlockStderr()
├── Io.unlockStderr()
Threaded.unlockStderr()
├── Io.Writer.flush()
│   Writer.defaultFlush()
│   File.Writer.drain()
│   File.Writer.drainStreaming()
│   File.writeStreaming()
│   Io.operate()
│   Threaded.operate()
│   Threaded.fileWriteStreaming()
│   posix.system.writev()
mutexUnlock()
```

