(defun delete-file-and-buffer ()
  "Delete the file and buffer you're on"
  (interactive)
  (let ((filepath (buffer-file-name)))
    (if filepath
        (if (y-or-n-p (concat "Really delete " filepath " ?"))
            (progn
              (kill-buffer)
              (ns-do-applescript (concat
                                  (format "set posixFile to POSIX file \"%s\"\n" filepath)
                                  "tell application \"Finder\"\n"
                                  "move posixFile to trash\n"
                                  "end tell")))))))
