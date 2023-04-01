local status, bufferline = pcall(require, "bufferline")
if (not status) then return end

local colors = require("catppuccin.palettes").get_palette "mocha"

local fg = colors.text
local bg = colors.base
local bg_dark = colors.mantle
local bg_light = colors.Surface1
local mauve = colors.mauve
local rosewater = colors.rosewater

-- TODO set Catppuccin colors
bufferline.setup({
  options = {
    always_show_bufferline = false,
    show_buffer_close_icons = false,
    show_close_icon = false,
    color_icons = true
  },
  highlights = {
    separator = {
      fg = mauve,
      bg = mauve,
    },
    separator_selected = {
      fg = rosewater,
    },
    background = {
      fg = fg,
      bg = bg_light
    },
    buffer_selected = {
      fg = fg,
      bold = true,
    },
    fill = {
      bg = bg_dark
    }
  },
})

vim.keymap.set('n', '<Tab>', '<Cmd>BufferLineCycleNext<CR>', {})
vim.keymap.set('n', '<S-Tab>', '<Cmd>BufferLineCyclePrev<CR>', {})
