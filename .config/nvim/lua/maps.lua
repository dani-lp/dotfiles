local keymap = vim.keymap

-- TODO choose keymaps
keymap.set('n', '<C-n>', '<cmd> NvimTreeToggle <CR>')
keymap.set({ 'n' }, '<C-S-j>', '<cmd> move+1 <CR>')
keymap.set({ 'n' }, '<C-S-k>', '<cmd> move-2 <CR>')
keymap.set('n', '<C-b>', '<cmd> bd <CR>')
