---
title: "flash.nvim with Neovim from Zero"
date: 2025-07-05 23:35:56
tags: ["notes", "julyfun", "25", "07"]
author: "julyfun-4070s-ubuntu2204"
os: "Linux julyfun-4070s-ubuntu 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Apr 22 19:00:15 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know: [computer]
---

本文假设你：
- 已经安装了 neovim
- 可能仅使用 neovim 的 init.vim
- 可能用过 easymotion

> vim 模式下，想要跳转到屏幕上某个随机位置，并不是很方便. `flash.nvim` 是一个理想选择，与 easymotion, leap.nvim 相似但是更符合直觉.

## 效果展示

假设当前状态如下，你想调到第一个 neovim 处：

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705233907.png)

按下: `/ n e o` 后，会在多个匹配 neo 的地方显示一个标识字母，按下 q 跳转到第一个 neo 处. 
> 注意，打下 `/ n` 就会开始匹配，你输入几个字母就匹配几个字母：
>
> 原有的 `/` 搜索功能不受影响.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705234039.png)

## 如何安装 (Starting from installing lazy.nvim)

> 注意 init.vim 和 init.lua 不能共存.
- 将你的 init.vim 改名为 init2.vim.
- 添加 init.lua 以及如下内容，它会加在你的 init2.vim，并安装 lazy.nvim 和 flash.nvim.

```lua
local vimrc = vim.fn.stdpath("config") .. "/init2.vim"
vim.cmd.source(vimrc)

-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  local lazyrepo = "https://github.com/folke/lazy.nvim.git"
  local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
  if vim.v.shell_error ~= 0 then
    vim.api.nvim_echo({
      { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
      { out, "WarningMsg" },
      { "\nPress any key to exit..." },
    }, true, {})
    vim.fn.getchar()
    os.exit(1)
  end
end
vim.opt.rtp:prepend(lazypath)

-- Make sure to setup `mapleader` and `maplocalleader` before
-- loading lazy.nvim so that mappings are correct.
-- This is also a good place to setup other settings (vim.opt)
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

-- Setup lazy.nvim
require("lazy").setup({
  spec = {
    -- add your plugins here
    -- [flash.nvim]
    {
      "folke/flash.nvim",
      event = "VeryLazy",
      ---@type Flash.Config
      opts = {},
      -- stylua: ignore
      keys = {
        { "/", mode = { "n", "x", "o" }, function() require("flash").jump() end, desc = "Flash" },
        { "s", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
        { "r", mode = "o", function() require("flash").remote() end, desc = "Remote Flash" },
        { "R", mode = { "o", "x" }, function() require("flash").treesitter_search() end, desc = "Treesitter Search" },
        { "<c-s>", mode = { "c" }, function() require("flash").toggle() end, desc = "Toggle Flash Search" },
      },
    }
  },
  -- Configure any other settings here. See the documentation for more details.
  -- colorscheme that will be used when installing plugins.
  install = { colorscheme = { "habamax" } },
  -- automatically check for plugin updates
  checker = { enabled = true },
})
```
- 重新启动 nvim，过一会儿就装好了.

## 其他功能

### flit 功能

这是默认开启的，可以增强你的 `f` 和 `F`. 
- 比如你正常地 `f{`，你就会正常跳到下一个 `{`（允许跨行）
- 光标后所有的 `{` 都会高亮。

