(global-set-key
 (kbd "<f9> w")
 (lambda ()
   (interactive)
   (save-buffer)
   (unless (buffer-modified-p)
     ((lambda ()
       (kill-buffer (buffer-name))
       (delete-frame))))))
