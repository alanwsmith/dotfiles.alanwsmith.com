;; list to hold the buffers to save
;; before earch run
(defvar aws-run-buffers (list))

;; this is where output goes to be read
;; by `tail -f` which is faster than
;; emacs and can handle large output
(defvar aws-run-tmp-file
  "/Users/alan/Desktop/emacs-log.log")

;; TODO: Update this so that it pushes to files
;; up in the list properly when you request
;; the same file multiple times to switch
;; back and forth.
;; this gets added by a hotkey
(defun aws-add-file-to-run-buffer ()
  (interactive)
  (add-to-list 'aws-run-buffers (buffer-name)))


;; This is what does the run 
(defun aws-run ()
  (interactive)
  ;; make a temporary list for the loop
  ;; since items need to be removed.
  ;; TODO: figure out if there's a
  ;; more concise way to do this that doesn't
  ;; require makeing a copy of the list. 
  (setq tmp-list (copy-list aws-run-buffers))
  (save-current-buffer 
    (while tmp-list 
      (when (get-buffer (car tmp-list))
        (with-current-buffer (car tmp-list)
          (save-buffer)
          )
        )
      (setq tmp-list (cdr tmp-list))
      )
    ;; call the first buffer in the list and
    ;; run it if it exists
    (when (get-buffer (car aws-run-buffers))
      (with-current-buffer (car aws-run-buffers)
        (call-process "chmod" nil nil nil "u+x" (buffer-file-name))
        (call-process (buffer-file-name) nil `(:file ,aws-run-tmp-file) nil)
        )
      )
    )
  )
