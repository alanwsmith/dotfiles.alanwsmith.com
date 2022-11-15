;; (add-hook
;;  'org-ctrl-c-ctrl-c-hook
;;  (function
;;   (lambda ()
;;   (setq original-content
;;         (org-element-property
;;          :value
;;          (org-element-at-point)))
;;   (setq updated-content 
;;         (with-temp-buffer 
;;           (insert original-content)
;;           (goto-char (point-min))
;;           (while (re-search-forward "\n\s+\n\\([[:alpha:]]\\)" nil t)
;;             (replace-match "\n\n\\1"))
;;           (goto-char (point-max))
;;           (when (looking-back "^\s+\n")
;;             (delete-region (match-beginning 0) (match-end 0)))
;;           (buffer-string)
;;           )
;;         )
;;   (save-excursion
;;     (goto-char (point-min))
;;     (while (re-search-forward original-content nil t)
;;       (replace-match updated-content t t))))))
