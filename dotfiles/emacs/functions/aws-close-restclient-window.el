(defun aws-close-restclient-window ()
  "Closes the window the restclient
opens when it runs in org-mode-bable.
The functionality is to grab the next
window in the window list, close it
and then return back to the original
window and buffer."

  (other-window 1)
  ;; (delete-window)

  ;; (message "---------------------")

  ;; This didn't do anything
  ;; (delete-other-windows (nth 1 (window-list)))

  ;; This closes the window but throws an error
  ;; (delete-window (nth 1 (window-list)))

  ;; (message "List: %s" (window-list))
  ;; (delete-window (nth 2 (window-list)))

  ;; This closes the buffer in the second window
  ;; but the window stays open showing the
  ;; scratch buffer
  ;; (quit-window t (nth 1 (window-list)))

  ;; ;; This didn't return anything
  ;; (message (window-atom-root
  ;;           (nth 0 (window-list))
  ;;           ))

  ;; this gets details for the main window
  ;; i think...
  ;; (message (window-parameters))


  ;; (message "List: %s" (window-list))
  ;; (message "Window: %s" (nth 1 (window-list)))
  ;; (message "%s" (window-parameters
  ;;            (nth 1 (window-list))
  ;;           ))
  ;; (message "%s" (window--check))
  ;; (message "ekekekek")

  ;; (message (window-list))
  ;; (message (nth 1 (window-list)))

  (message "yryryyryr")

  ;; (with-selected-window
  ;;     (nth 0 (window-list))
  ;;    (
  ;;     (message "22222")
  ;;     ;; (delete-window)
  ;;     ;; (nth 1 (window-list))
  ;;     )
  ;;    )

  )



;; (add-hook 'restclient-response-received-hook
;;           'aws-close-restclient-window-2
;;           )


;; (add-hook 'restclient-response-loaded-hook
;;           'aws-close-restclient-window
;;           )



;; (prin1 (get-buffer-window))
;; (selected-window)

