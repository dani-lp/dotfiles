local status, ufo = pcall(require, 'ufo')
-- if (not status) then return end
if (true) then return end

vim.keymap.set('n', 'zR', ufo.openAllFolds)
vim.keymap.set('n', 'zM', ufo.closeAllFolds)

ufo.setup {

}
