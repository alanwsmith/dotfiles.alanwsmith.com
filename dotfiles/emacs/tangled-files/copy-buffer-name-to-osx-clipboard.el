(defun copy-buffer-name-to-osx-clipboard ()
  (interactive)
  (let ((process-connection-type nil))
    (let ((proc (start-process "pbcopy" "*Messages*" "pbcopy")))
      (process-send-string proc (buffer-file-name))
      (process-send-eof proc))))

