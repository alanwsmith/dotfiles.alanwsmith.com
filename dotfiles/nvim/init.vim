
" Turn on line numbers
set nu

" Make line numbers relative
set rnu

" Disable the mouse
set mouse=

" Copy and paste to the sytem clipboard
set clipboard+=unnamedplus


" TODO - note what these each do
set tabstop=2
set shiftwidth=2
set softtabstop=2
set autowrite
set autoread
set nowrap
set expandtab
set smarttab
set autoindent
set smartindent
" set copyindent
set shiftround
set smartcase
set incsearch
set spell


" stop highlighting matching brackets
let loaded_matchparen = 1

" change the leader to the comma
let mapleader=','

" turn off the highlight for all matching searches that never
" seems to want to go away
set hlsearch!

" This is what allows you to hit the escape key and immediately
" be able to hit the leader key. Without it, you either have to
" hit escape twice, hit leader twice, or wait a full second 
" before hitting leader.
set timeoutlen=1000 ttimeoutlen=10


call plug#begin("~/.vim/plugged")

    " Install new plugins with :PlugInstall
    " Remove plugs by taking them out of this config then
    " running :PlugClean

    " Prettier
    Plug 'prettier/vim-prettier', {
    \ 'do': 'yarn install',
    \ 'for': ['javascriptreact', 'typescriptreact', 'javascript', 'typescript', 'css', 'less', 'scss', 'json', 'graphql', 'markdown', 'vue', 'svelte', 'yaml', 'html', 'tsx'] }



    " Tree sitter which is configured below for highlighting
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}

    " nvim-tree for file browsing
    " Plug 'nvim-tree/nvim-web-devicons' " optional, for file icons
    " Plug 'nvim-tree/nvim-tree.lua'

    " lets you do comments quickly with `gcap`
    Plug 'tpope/vim-commentary'

    " For Rust Analyzer:
    Plug 'rust-lang/rust.vim'
    Plug 'neovim/nvim-lspconfig'
    Plug 'simrat39/rust-tools.nvim'


call plug#end()

lua <<EOF
local rt = require("rust-tools")
rt.setup({
  server = {
    on_attach = function(_, bufnr)
      -- Hover actions
      vim.keymap.set("n", "<C-space>", rt.hover_actions.hover_actions, { buffer = bufnr })
      -- Code action groups
      vim.keymap.set("n", "<Leader>a", rt.code_action_group.code_action_group, { buffer = bufnr })
    end,
  },
})

EOF


" Let prettier autoformat on save
" Looks like you need both of these to make it work
let g:prettier#autoformat = 1
let g:prettier#autoformat_require_pragma = 0
let g:prettier#quickfix_enabled=0
command! -nargs=0 Prettier :CocCommand prettier.formatFile


" lua <<EOF
" require'nvim-treesitter.configs'.setup {
"     -- A list of parser names, or "all"
"     ensure_installed = { "javascript", "c", "lua", "rust", "json", "python", "typescript" },
"     sync_install = false,
"     auto_install = true,
"     highlight = {
" 	enable = true,
" 	additional_vim_regex_highlighting = false
"     },
" }
" EOF

" " nvim-tree configuration 
" lua <<EOF
"     vim.g.loaded_netrw = 1
"     vim.g.loaded_netrwPlugin = 1
"     vim.opt.termguicolors = true
"     require("nvim-tree").setup()
" EOF



" Setup so `:te` is aliased to expand to `:tabedit`
cnoreabbrev <expr> te getcmdtype() == ":" && getcmdline() == 'te' ? 'tabedit' : 'te'

" Save all files with `,s`
map <leader>s :wa<cr>

" This is how you can auto switch between relative and 
" absolute line numbers depending on which mode you're in
" It does cause flashing of the line numbers though, so 
" not sure if I'm going to keep it. 
set number
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu && mode() != "i" | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu                  | set nornu | endif
augroup END

" Keep lines above and below the cursor
set scrolloff=5



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""" ONLY HAVE ONE OF THESE UNCOMMENTED AT A TIME
" This is what lets you run files stuff directly. 
" TODO is to switch this so it figure out what the language 
" is automatically

"""""" Python testing - 
"" 
map <leader>m :let $RUN_THIS = expand('%:p')<cr>
map <leader>r :!if [ $RUN_THIS ]; then python3 "${RUN_THIS}"; else python3 %; fi<cr>
map <leader>R :!python3 %<cr>


" map <leader>r :!cargo run<cr>

""""" JavaScript runner
" map <leader>r :!node %<cr>
" map <leader>j :!/usr/bin/env node %<cr>
" map <leader>r :!./%<cr>

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


" Make background transparent
hi Normal guibg=NONE 
hi Normal ctermbg=NONE


" This is how you can auto switch between relative and 
" absolute line numbers depending on which mode you're in
" It does cause flashing of the line numbers though, so 
" not sure if I'm going to keep it. 
set number
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu && mode() != "i" | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu                  | set nornu | endif
augroup END


" You can use this to auto save files when nvim loses focus. 
" I'm not using it right now becuase I'm in such the habbit 
" of saving I don't know if I need it, but I'll think more about
" it now that I know it exists. I think there is an issue if you 
" have an unsaved buffer. I'll look into that if I hit it. 
" via: https://vim.fandom.com/wiki/Auto_save_files_when_focus_is_lost
" :au FocusLost * :wa


" let g:rustfmt_autosave = 1

let g:rustfmt_autosave = 1
