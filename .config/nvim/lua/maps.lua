vim.g.mapleader = ' '

vim.keymap.set('n', '<C-n>', '<cmd> NvimTreeToggle <CR>')
vim.keymap.set({ 'n' }, '<C-S-j>', '<cmd> move+1 <CR>')
vim.keymap.set({ 'n' }, '<C-S-k>', '<cmd> move-2 <CR>')
vim.keymap.set('n', '<C-b>', '<cmd> bd <CR>')
-- keymap.set('n', '...TBD...', '<cmd> lua vim.lsp.buf.code_action() <CR>')

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv") -- move lines in visual mode
vim.keymap.set("v", "K", ":m '>-2<CR>gv=gv")

vim.keymap.set("x", "<leader>p", "\"_dP")   -- paste without loosing clipboard

vim.keymap.set("n", "<leader>y", "\"+y")  -- yank into system clipboard
vim.keymap.set("v", "<leader>y", "\"+y")  -- yank into system clipboard
vim.keymap.set("n", "<leader>Y", "\"+Y")  -- yank into system clipboard

vim.keymap.set("n", "Q", "<nop>")   -- unbind "Q"

