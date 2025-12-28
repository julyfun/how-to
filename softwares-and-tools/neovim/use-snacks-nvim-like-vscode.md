---
title: "Use snacks.nvim like VSCode"
date: 2025-12-20 03:51:15
tags: ["softwares-and-tools", "neovim"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-90-generic #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
confidence: 2
---

- Show entire diagnostics:
    - `:lua vim.diagnostic.open_float()`
    - ref: https://www.reddit.com/r/neovim/comments/18qh3mg/how_to_show_entire_diagnostic_message/

## Panels & bars
- terminal: <C-/>

## Info
- [useless] Show current file abs path: `:!echo %:p` ref: https://vi.stackexchange.com/a/1885
- Show keymap: `<leader>sk`
- Show inlay hints: `<leader>uh`
### Info.notification
- Show notification: `<leader>n`
- clear notification: `<leader>un`

## Edit
- Rename symbol: `:lua vim.lsp.buf.rename()`

## rust.info
- :RustLsp expandMacro

