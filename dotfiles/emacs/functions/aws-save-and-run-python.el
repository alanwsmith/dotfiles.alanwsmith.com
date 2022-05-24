(defun aws-save-and-run-python (arg)
  "Copy of spacemacs/python-execute-file that saves
the file before compiling and executing. Original source
is: https://github.com/syl20bnr/spacemacs/blob/b3e67aafe2451ca91e2d310d29879616e10981d0/layers/%2Blang/python/funcs.el#L519"

  (interactive "P")
  (save-buffer)
  (setq python-shell-interpreter "/opt/homebrew/bin/python3")
  (let ((universal-argument t)
        (compile-command
         (format
          "%s %s"
          (spacemacs/pyenv-executable-find python-shell-interpreter)
          (shell-quote-argument
           (file-name-nondirectory buffer-file-name)))))
    (if arg
        (call-interactively 'compile)
      (compile compile-command t)
      (with-current-buffer (get-buffer "*compilation*")
        (inferior-python-mode)))))
)
