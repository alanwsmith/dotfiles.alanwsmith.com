;; :tangle ~/workshop/dotfiles.alanwsmith.com/dotfiles/emacs/tangled-files/python-source-block-fix.el

;; (add-hook
;;  'org-ctrl-c-ctrl-c-hook
;;  (function
;;   (lambda ()
;;     (replace-regexp-in-region
;;      "\s+\n"
;;      "\n"
;;      (org-element-property :begin
;;                            (org-element-at-point))
;;      (org-element-property :end
;;                            (org-element-at-point)))
;;     nil)))



;; (with-temp-buffer 
;;   (insert "the quick brown fox\n")
;;   (insert "     \n")
;;   (insert "the quick brown fox\n")
;;   (goto-char (point-min))
;;   (while (re-search-forward "\n\s+\n\\([[:alpha:]]\\)" nil t)
;;     (replace-match "\n\n\\1"))
;;   (princ (buffer-string))
;;   )




;; (defun fix-python-index ()
;;   (interactive)
;;   (message "alpha")
;;   (replace-regexp-in-region
;;    "\n\s+\n\\([[:alpha:]]\\)" 
;;    "\n\n\\1"
;;    (org-element-property :begin
;;                          (org-element-at-point))
;;    (org-element-property :end
;;                          (org-element-at-point)))
;;   (goto-char (point-max))
;;   (org-ctrl-c-ctrl-c)
;;   (message "bravo")
;;   )


;; (global-set-key (kbd "C-M-@") 'fix-python-index)
