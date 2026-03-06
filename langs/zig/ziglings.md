---
title: "ziglings"
date: 2026-03-05 08:30:46
tags: ["langs", "zig"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 25.2.0 Darwin Kernel Version 25.2.0: Tue Nov 18 21:09:55 PST 2025; root:xnu-12377.61.12~1/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

## sentinels (f10:45)

```zig
//     const a: [4:0]u32       =  [4:0]u32{1, 2, 3, 4};
是 .array, 额外存储 0 和长度
//     const b: [:0]const u32  = &[4:0]u32{1, 2, 3, 4};
是 .slice，必须指向 0 结尾的 array
//     const c: [*:0]const u32 = &[4:0]u32{1, 2, 3, 4};
是 .pointer，末端必须 0
```

- 如何拿以上的 typeinfo?
```zig
(my_seq: anytype)
const my_typeinfo = @typeInfo(@TypeOf(my_seq));
    switch (my_typeinfo) {
        .array => {
            ...
        },
        .pointer => {
            ...
        },
        else => unreachable,
```

