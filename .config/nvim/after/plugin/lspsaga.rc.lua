local status, saga = pcall(require, 'lspsaga')
if (not status) then return end

saga.setup {
  server_filetype_map = {}
}

local opts = { noremap = true, silent = true }
vim.keymap.set('n', '<C-j>', '<cmd>Lspsaga diagnostic_jump_next<cr>', opts)
vim.keymap.set('n', '<C-l>', '<cmd>Lspsaga hover_doc<cr>', opts)
vim.keymap.set('n', '<C-x>', '<cmd>Lspsaga peek_type_definition<cr>', opts)
vim.keymap.set('n', '<gd>', '<cmd>Lspsaga lsp_finder<cr>', opts)
vim.keymap.set('n', '<gp>', '<cmd>Lspsaga signature_help<cr>', opts)
vim.keymap.set('n', '<C-k>', '<cmd>Lspsaga peek_definition<cr>', opts)
vim.keymap.set('n', '<gr>', '<cmd>Lspsaga rename<cr>', opts)
