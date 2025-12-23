---
title: flash.nvim with Neovim from Zero
date: 2025-07-05 23:35:56
tags:
  - "25"
  - neovim
  - vim
  - flash.nvim
  - vim-search
  - lazy.nvim
author: julyfun-4070s-ubuntu2204
os: "Linux julyfun-4070s-ubuntu 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Apr 22 19:00:15 UTC 2 x86_64 x86_64 x86_64 GNU/Linux"
assume-you-know:
  - neovim and init.vim basic usage
---

vim 模式下，想要跳转到屏幕上某个随机位置，并不是很方便. `flash.nvim` 是一个理想选择，与 easymotion, leap.nvim 相似但是更符合直觉.

本文假设你：
- 已经安装了 neovim
- 可能仅使用 neovim 的 init.vim
- 可能用过 easymotion

## flash.nvim 效果展示

假设当前状态如下，光标在第 18 行，你想跳到第一个 `neovim`：

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705233907.png)

按下 `/ n e o` 后，会在所有匹配 `neo` 的地方显示一个标识字母，按下 `q` 跳转到第一个 `neo` 处：

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705234039.png)

> 其实打下 `/ n` 就会开始匹配，你输入几个字母就匹配几个字母. 原有的 `/` 搜索功能不受影响.

## 如何安装 (Starting from installing lazy.nvim)

> 注意 init.vim 和 init.lua 不能共存.
- 将你的 init.vim 改名为 init2.vim.
- 创建 init.lua，添加如下内容，它会加在你的 init2.vim，并安装 lazy.nvim 和 flash.nvim.

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
      opts = {
        modes = {
          search = { enabled = true }
        }
      },
      -- stylua: ignore
      keys = {
        { "s", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
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
> 基于 flash.nvim 文档改动. `search = { enabled = true }` 这一行开启了 search 增强.
>
> `<c-s>` 似乎是用于 Toggle flash.nvim.

- 添加上述脚本后，重新启动 nvim，会弹出安装窗口，过一会儿就装好了.

## 其他功能

### flit 功能

**推荐.** 这是默认开启的，可以增强你的 `f` 和 `F`.
- 比如你正常地 `f{`，你就会跳到后面第一个 `{`（允许跨行）
- 此时第一个 `{` 后所有的 `{` 都会高亮，如果你想跳到的其实是第三个 `{`，那么再按两次 `f`. 
- 不喜欢这个功能的话上面配置里的 `opts = {}` 可以加入:
```lua
opts = {
  modes = {
    char = { enabled = false }
  }
},
```

### treesitter 功能

**推荐.** 在支持 treesitter 的环境下按下 `s` 可以显示附近作用域的首尾，按下 label 跳转过去.

![](https://how-to-1258460161.cos.ap-shanghai.myqcloud.com/how-to20250705235815.png)

### remote 功能

**不推荐**，会 Ctrl + O 就用不着. 所以上面配置中我没有引入该功能.

## Postscript

- 搜索功能正常支持中文字符.
- vim 插件我认为应该和 vim 原有键位贴近，不能离开了这个功能就不会用 vim 了，毕竟我们经常要在新电脑上用 vi 编辑东西.
- 如果 git clone failed / checkout failed，可以尝试 .gitconfig 中加入 URL 替换 (works on my mac m1).

```gitconfig
[url "git@github.com:"]
    insteadOf = https://github.com/

[url "git@github.com:"]
    insteadOf = git://github
```

