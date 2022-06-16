;; TODO: Clear out this file when `aws-run`'' is done in
;; the `grim- Run Command SEtup' file is done. (though
;; the filename might change)

;; ---------------------------------

;; Remember that this file sticks arround until it gets cleaned
;; up by what ever sweeps the tmp directory so beware of
;; using it for sensitive data without cleaning it.

;; (defvar aws-run-python-tmp-file "/tmp/aws-run-python-tmp")

;; (defun aws-run-python ()
;;   (interactive)
;;   (save-buffer)
;;   (call-process
;;    "/bin/bash"
;;    nil
;;    nil
;;    nil
;;    "-c"
;;    (concat
;;    "/opt/homebrew/bin/python3"
;;    " "
;;    (buffer-file-name)
;;    " "
;;    aws-run-python-tmp-file
;;    )
;;    )
;;    (call-process
;;    "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
;;    ;; "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"
;;     nil
;;     nil
;;     nil
;;     aws-run-python-tmp-file
;;     )
;;    )
