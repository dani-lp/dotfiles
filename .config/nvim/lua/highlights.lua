vim.opt.cursorline = true
vim.opt.termguicolors = true
vim.opt.winblend = 0
vim.opt.wildoptions = 'pum' -- tf is this
vim.opt.pumblend = 5
vim.opt.background = 'dark'

local colors = require("catppuccin.palettes").get_palette "mocha"

local darker_black = colors.crust
local black = colors.base
local black2 = colors.surface0
local white = colors.text
local red = colors.red
local green = colors.green

-- Telescope
local fg_bg = function(group, fgcol, bgcol)
  vim.cmd("hi " .. group .. " guifg=" .. fgcol .. " guibg=" .. bgcol)
end

local bg = function(group, col)
  vim.cmd("hi " .. group .. " guibg=" .. col)
end

local fg = function(group, col)
  vim.cmd("hi " .. group .. " guifg=" .. col)
end


fg_bg("TelescopeBorder", darker_black, darker_black)
fg_bg("TelescopePromptBorder", black2, black2)

fg_bg("TelescopePromptNormal", white, black2)
fg_bg("TelescopePromptPrefix", red, black2)

bg("TelescopeNormal", darker_black)

fg_bg("TelescopePreviewTitle", black, green)
fg_bg("TelescopePromptTitle", black, red)
fg_bg("TelescopeResultsTitle", darker_black, darker_black)

bg("TelescopeSelection", black2)
