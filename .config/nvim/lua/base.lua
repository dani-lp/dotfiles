vim.cmd('autocmd!')

vim.scriptencoding = 'utf-8'
vim.opt.encoding = 'utf-8'
vim.opt.fileencoding = 'utf-8'

vim.wo.number = true

-- to see the full list of settings, :help option-list
vim.opt.title = false
vim.opt.autoindent = true
vim.opt.hlsearch = false
vim.opt.incsearch = true
vim.opt.backup = false
vim.opt.showcmd = true
vim.opt.cmdheight = 1
vim.opt.laststatus = 2
vim.opt.expandtab = true -- use spaces when <Tab> is inserted
vim.opt.scrolloff = 10
vim.opt.shell = 'fish'
vim.opt.ignorecase = true
vim.opt.smarttab = true
vim.opt.breakindent = true
vim.opt.shiftwidth = 2
vim.opt.tabstop = 2
vim.opt.ai = true -- Auto indent
vim.opt.si = true -- Smart indent
vim.opt.wrap = true -- Wrap lines
vim.opt.backspace = 'start,eol,indent'
vim.opt.relativenumber = true
vim.opt.termguicolors = true

-- colorsheme stuff - move to another place
vim.g.catppuccin_flavour = "mocha"
require('catppuccin').setup()
vim.cmd [[colorscheme catppuccin]]

-- the catppuccin colors leave the line numbers too dark
-- so this lightens them up to make them more legible
vim.api.nvim_create_autocmd("ColorScheme", {
  pattern = "*",
  callback = function()
    vim.api.nvim_set_hl(0, "LineNr", { fg = "#9399b2" })
  end
})
