(defun open-buffer-in-new-frame ()
  "Open the current buffer in a new frame"
  (interactive)
  (let ((this-frame-buffer nil))
    (setq this-frame-buffer (car (frame-parameter nil 'buffer-list)))
    (make-frame)
    (switch-to-buffer this-frame-buffer)
    )

  ; (make-frame)
  ; (display-buffer-pop-up-frame (buffer-name) ())
  ; (make-frame (buffer-name) )
  ; (clone-frame)
  ; (aws-frame-bump)
  ; (set-frame-parameter nil 'top aws-frame-base-top)
  ; (set-frame-parameter nil 'left aws-frame-base-left)

  )
