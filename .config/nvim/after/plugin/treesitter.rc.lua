local status, ts = pcall(require, 'nvim-treesitter.configs')
if (not status) then return end

ts.setup {
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
  indent = {
    enable = true,
    disable = {},
  },
  ensure_installed = {
    'css',
    'json',
    'html',
    'markdown',
    'markdown_inline',
    'lua',
    'rust',
    'python',
    'tsx',
  },
  autotag = {
    enable = true,
  }
}
