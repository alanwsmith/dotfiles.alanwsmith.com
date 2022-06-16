;; TODO:
;; Clear this files. the functionality is now being
;; handled by the `aws-run' function in
;; `grim- Run Command Setup.txt' (though
;; that file name will likely change)

;; -------------------

;; The goal here is to make it easy to hit a single
;; not key to run files

;; Tried to setup a varaible for the log file, but couldn't
;; get it to work. See:
;; https://emacs.stackexchange.com/q/71942/38139


;; (defvar save-and-run-output-app
;;   "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" 
;;   "The application to use to open the
;; output file"
;;   )


;; (defvar save-and-run-output-path
;;   "/Users/alan/Desktop/emacs-log.txt"
;;   "Output location for the tmp file to use"
;;   )

;; (defun save-and-run-file (arg) "Save and run a file"
;;        (interactive "P")
;;        (save-buffer)
;;        (call-process (shell-quote-argument buffer-file-name) nil `(:file ,save-and-run-output-path))
;;        ; (call-process save-and-run-output-app nil nil nil "/Users/alan/Desktop/emacs-log.txt")
;;        ; (call-process "osascript" nil nil nil "-l" "JavaScript" "-e" "var emacs = new Application('Emacs'); emacs.activate()")
;;        )

;; (add-hook 'python-mode-hook
;;           (lambda () (local-set-key (kbd "s-r") 'save-and-run-file))
;;           )

;; (add-hook 'js2-mode-hook
;;           (lambda () (local-set-key (kbd "s-r") 'save-and-run-file))
;;           )

