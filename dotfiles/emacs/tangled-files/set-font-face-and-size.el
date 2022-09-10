(defun set-font-face-and-size (name size)
  "Sets the font size for open and new frames"
  (let ((new-font-string (concat
                      "-*-"
                      name
                      "-normal-normal-normal-*-"
                      (number-to-string size)
                      "-*-*-*-m-0-iso10646-1")))
    (set-face-attribute 'default nil :font
                        new-font-string
                        )
    (setq default-frame-alist (assoc-delete-all 'font default-frame-alist))
    (add-to-list 'default-frame-alist 
                 `(font . ,new-font-string))))
