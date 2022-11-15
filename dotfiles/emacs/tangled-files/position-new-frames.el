;; (defvar aws-frame-base-top 80
;;   "This is the number of pixels down that
;; new frames start to render at and get
;; reset to when they have pushed past
;; the value of `aws-frame-max-top`"
;;   )
;; (defvar aws-frame-base-left 60
;;   "Starting and result postion for the
;; left side of new frames"
;;   )
;; (defvar aws-frame-max-top 220
;;   "Max push of new frames from the top"
;;   )
;; (defvar aws-frame-max-left 420
;;   "Max push of new frames to the left"
;;   )
;; ;; initial values 
;; (defvar aws-frame-top 80)
;; (defvar aws-frame-left 60)
;; (defvar aws-frame-width 140)
;; (defvar aws-frame-height 58)
;; (defun aws-frame-bump ()
;;   "Sets up variables to be ready to
;; open the next frame"
;;   (if (>= aws-frame-top aws-frame-max-top)
;;       (setq aws-frame-top aws-frame-base-top)
;;     (setq aws-frame-top (+ aws-frame-top 60))
;;     )
;;   (if (>= aws-frame-left aws-frame-max-left)
;;       (setq aws-frame-left aws-frame-base-left)
;;     (setq aws-frame-left (+ aws-frame-left 60))
;;     )
;;   ;; This delete has to happen other wise the duplicate
;;   ;; values aren't put on the alist when the frames
;;   ;; cycle arround
;;   (delete `(top . ,aws-frame-top) default-frame-alist)
;;   (delete `(left . ,aws-frame-left) default-frame-alist)
;;   (add-to-list 'default-frame-alist `(top . ,aws-frame-top))
;;   (add-to-list 'default-frame-alist `(left . ,aws-frame-left))
;;   (add-to-list 'default-frame-alist `(width . ,aws-frame-width))
;;   (add-to-list 'default-frame-alist `(height . ,aws-frame-height))
;;   )
;; (add-to-list 'before-make-frame-hook 'aws-frame-bump)
