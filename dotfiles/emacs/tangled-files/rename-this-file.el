(defun rename-this-file ()
  (interactive)
  (let (
        (working-directory
         (file-name-directory buffer-file-name))
        (current-file-path
         (buffer-file-name))
        (new-file-name 
         (concat
          (read-from-minibuffer "New file name: ")
          ".org")))
    (let
        ((new-file-path
          (concat working-directory new-file-name)))
      (progn
        (save-buffer)
        (kill-buffer)
        (rename-file current-file-path new-file-path)
        (find-file new-file-path)
        )
    )))
