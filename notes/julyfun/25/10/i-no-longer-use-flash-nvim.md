---
title: "I no longer use flash.nvim"
date: 2025-11-19 10:18:36
tags: ["notes", "julyfun", "25", "10"]
author: "Julyfun MacOS14.5 M1"
os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
assume-you-know: [computer]
confidence: 2
---

Slash search is now ok for me. And vscode doesn't have a good flash.nvim.

```lua
-    -- [cursor]
-    {
-      "folke/flash.nvim",
-      event = "VeryLazy",
-      ---@type Flash.Config
-      opts = {
-        modes = {
-          search = { enabled = true }
-        }
-      },
-      -- stylua: ignore
-      keys = {
-        { "s", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
-        { "<c-s>", mode = { "c" }, function() require("flash").toggle() end, desc = "Toggle Flash Search" },
-      },
-    },
```

