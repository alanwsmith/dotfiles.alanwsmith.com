(add-hook 'org-mode-hook
          (lambda ()
            (display-line-numbers-mode +1)
            (setq display-line-numbers 'relative)
            ))

(add-hook 'emacs-lisp-mode-hook
          (lambda ()
            (display-line-numbers-mode +1)
            (setq display-line-numbers 'relative)
            ))

(add-hook 'python-mode-hook
          (lambda ()
            (display-line-numbers-mode +1)
            (setq display-line-numbers 'relative)
            (show-paren-mode -1)
            ))

(add-hook 'js2-mode-hook
          (lambda ()
            (display-line-numbers-mode +1)
            (setq display-line-numbers 'relative)
            ))

;; TODO: see if this works for html pages
(add-hook 'web-mode-hook
          (lambda ()
            (display-line-numbers-mode +1)
            (setq display-line-numbers 'relative)
            ))
