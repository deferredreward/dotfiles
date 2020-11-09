" Functionality for taking notes
" Author: Rafael Cavalcanti - rafaelc.org

let g:notes_dir='~/.data/Sync/.Notes/'
let g:notes_resources_dir='~/.data/Sync/.Notes/_resources'

" md-img-paste: Save images to resources folder
autocmd BufNewFile,BufRead ~/.data/Sync/.Notes/*
	\ let g:mdip_imgdir_absolute = g:notes_resources_dir |
	\ let g:mdip_imgdir = g:notes_resources_dir |
	\ let g:mdip_imgdir_intext = g:notes_resources_dir

" fzf: Set special keybinds to search notes
command! -bang NFiles call fzf#vim#files(g:notes_dir, {'options': ['--layout=reverse', '--info=inline', '--preview', '~/.vim/plugged/fzf.vim/bin/preview.sh {}']}, <bang>0)
noremap <C-n> :NFiles<CR>
