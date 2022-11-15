(defun get-end-data ()
  (save-buffer)
  (setq originalBuffer (buffer-file-name))
  (with-temp-buffer
    (insert-file-contents originalBuffer)
    (goto-char (point-max))
    (if (search-forward "__END__" nil (message "ERROR: No END at the bottom of the file") -1)
        ((lambda ()
           (goto-char (point-max))
           (delete-region
            (point-min) 
            (search-forward "__END__" nil nil -1))
           (delete-region
            (point-min) 
            (search-forward "__END__\n" nil nil))
           (string-trim
            (buffer-substring-no-properties
             (point-min)
             (point-max)
             ))))
      (princ "ERROR: No END data section at the bottom of the file")
      )))
