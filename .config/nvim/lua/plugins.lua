local status, packer = pcall(require, 'packer')
if (not status) then
  print('Packer is not installed!')
  return
end

vim.cmd [[packadd packer.nvim]]

packer.startup(function(use)
  use 'wbthomason/packer.nvim'           -- package manager
  use {
    'catppuccin/nvim', as = 'catppuccin' -- theme
  }
  use {
    'nvim-telescope/telescope.nvim',
    tag = '0.1.0',
    requires = { { 'nvim-lua/plenary.nvim' } }
  }
  use {
    'nvim-lualine/lualine.nvim', -- bottom line
    requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }
  use {
    'nvim-treesitter/nvim-treesitter', -- syntax highlighting
    run = ':TSUpdate'
  }

  -- LSP configuration
  use {
    'VonHeikemen/lsp-zero.nvim',
    branch = 'v2.x',
    requires = {
      -- LSP Support
      { 'neovim/nvim-lspconfig' }, -- Required
      {
        -- Optional
        'williamboman/mason.nvim',
        run = function()
          pcall(vim.cmd, 'MasonUpdate')
        end,
      },
      { 'williamboman/mason-lspconfig.nvim' }, -- Optional

      -- Autocompletion
      { 'hrsh7th/nvim-cmp' },     -- Required
      { 'hrsh7th/cmp-nvim-lsp' }, -- Required
      { 'L3MON4D3/LuaSnip' },     -- Required
    }
  }

  use {
    'kyazdani42/nvim-tree.lua',       -- file tree
    requires = {
      'kyazdani42/nvim-web-devicons', -- optional, for file icons
    },
    tag = 'nightly'                   -- optional, updated every week. (see issue #1193)
  }
  use 'onsails/lspkind-nvim'          -- vscode-like pictograms
  use 'hrsh7th/cmp-buffer'            -- nvim-cmp source for buffer words
  use 'windwp/nvim-autopairs'
  use 'windwp/nvim-ts-autotag'
  use 'nvim-telescope/telescope-file-browser.nvim'
  use 'kyazdani42/nvim-web-devicons' -- File icons
  use 'norcalli/nvim-colorizer.lua'
  use 'lewis6991/gitsigns.nvim'
  use 'glepnir/lspsaga.nvim' -- LSP UIs
  use {
    'folke/todo-comments.nvim',
    requires = 'nvim-lua/plenary.nvim'
  }
  use 'numToStr/Comment.nvim'
  use 'akinsho/nvim-bufferline.lua'
  use { 'kevinhwang91/nvim-ufo', requires = 'kevinhwang91/promise-async' }
  use({
    "kylechui/nvim-surround",
    tag = "*", -- Use for stability; omit to use `main` branch for the latest features
    config = function()
      require("nvim-surround").setup({})
    end
  })
  use {
    "folke/trouble.nvim",
    requires = "kyazdani42/nvim-web-devicons",
  }
  use 'RRethy/vim-illuminate'
  use 'echasnovski/mini.nvim'
  use { 'neoclide/coc.nvim', branch = 'release' }
  use "nullchilly/fsread.nvim"
  use({
    'simrat39/rust-tools.nvim',
    config = function()
      require("rust-tools").setup({})
    end
  })
end)
