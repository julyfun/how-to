---
title: "Compiler PKU"
date: 2025-12-25 03:32:10
tags: ["25", "12"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-90-generic #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

bookmark
- https://pku-minic.github.io/online-doc/#/lv3-expr/

execute
- `docker run -it --rm -v /home/julyfun/Documents/GitHub/julyfun/compiler/:/root/compiler maxxing/compiler-dev bash`
- `cargo run -- -koopa hello.c -o hello.koopa`

测试数据:
- docker /opt/bin/testcases

## Lv0
## Lv1
- sysy: C-like lang for education
## Lv1.4
Koopa Ir 内存形式没文档. [○･｀Д´･ ○]

```rust
// WRONG
let mut main = FunctionData::new(...);
let zero = main.new_value().integer(0);  // globals 还没初始化, globals.upgrade() 会 panic
let main = program.new_func(main);       // 太晚了

// RIGHT
let main_data = FunctionData::new(...);
let main_func = program.new_func(main_data);  // 先添加，初始化 globals
let main = program.func_mut(main_func);       // 获取可变引用
let zero = main.new_value().integer(0);       // 现在 globals 已经设置好了
```

Result:
```console
root@4c93081a761b:~/compiler# cat hello.koopa
fun @main(): i32 {
%entry:
  ret 32
}


    Finished `release` profile [optimized] target(s) in 5.61s
running test "0_main" ... PASSED
running test "1_comments" ... PASSED
running test "2_int_dec" ... PASSED
running test "3_int_oct" ... PASSED
running test "4_int_hex" ... PASSED
running test "5_compact" ... PASSED
running test "6_whitespaces" ... PASSED
PASSED (7/7)
```

顺便就配了一大堆 NVIM.

## Lv2

注意 Value 类型是一个指针. dfg.value(*self); 可以获取实际 ValueData. 然后可以 `match data.kind()`

