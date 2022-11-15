;; These are numbers, best place to make temp changes
(global-set-key (kbd "C-M-!") 'copy-buffer-name-to-osx-clipboard)




;; C-M-S-h is for when Emacs is already active
;; C-M-S-i catches the signal that's passed from
;; Alfred when C-M-S-h is triggered outside of Emacs
(global-set-key (kbd "C-M-S-h") 'grimoire-mode-search)
(global-set-key (kbd "C-M-S-i") 'grimoire-mode-search)

(global-set-key (kbd "C-M-S-t") 'org-babel-tangle)

;; Execute a source block (closing the error window first
;; if it's open
;; (global-set-key (kbd "C-M-S-f") 'org-ctrl-c-ctrl-c)
(global-set-key (kbd "C-M-S-f") 'close-error-window-and-run)

;; Execute all source blocks in a buffer
(global-set-key (kbd "C-M-S-a") 'spacemacs/add-word-to-dict-global)
(global-set-key (kbd "C-M-S-b") 'org-babel-execute-buffer)

(global-set-key (kbd "C-M-S-n") 'rename-this-file)

(global-set-key (kbd "C-M-S-q") 'open-buffer-in-new-frame)
(global-set-key (kbd "C-M-S-z") 'helm-for-files)



;; This is the more advanced run. Need to document it.
;; (global-set-key (kbd "C-M-S-r") 'aws-run )
;; (global-set-key (kbd "<f9> 9") 'aws-add-file-to-run-buffer)

;; (global-set-key (kbd "<f9> <left>") 'previous-buffer)
;; (global-set-key (kbd "<f9> <right>") 'next-buffer)


;;;;;;;;
;; Keys that aren't mapped directly on the moonlander


(global-set-key (kbd "C-M-S-l") 'not-mapped-on-moonlander)
(global-set-key (kbd "C-M-S-m") 'not-mapped-on-moonlander)
(global-set-key (kbd "C-M-S-u") 'not-mapped-on-moonlander)
(global-set-key (kbd "C-M-S-v") 'not-mapped-on-moonlander)
(global-set-key (kbd "C-M-S-w") 'not-mapped-on-moonlander)
