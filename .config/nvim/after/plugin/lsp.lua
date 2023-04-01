local status, lsp = pcall(require, 'lsp-zero')
if (not status) then return end

lsp.preset('recommended')
lsp.setup()

lsp.ensure_installed({
  'eslint',
  'pyright',
  'rust_analyzer',
  'sumneko_lua',
  'tsserver',
})

-- local cmp_status, cmp = require('cmp')
-- if (not cmp_status) then return end
-- local cmp_select = { behavior = cmp.SelectBehavior.Select }
-- local cmp_mappings = lsp.defaults.cmp_mappings({
--
-- })

lsp.set_preferences({
  sign_icons = {}
})

-- lsp.setup_nvim_cmp({
--   mapping = cmp_mappings
-- })

lsp.on_attach(function(client, bufnr)
  local opts = { buffer = bufnr, remap = false }
end)
