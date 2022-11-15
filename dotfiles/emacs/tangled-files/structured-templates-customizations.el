  (require 'org-tempo)

  (setq org-structure-tempate-alist (assoc-delete-all "l" org-structure-template-alist))
  (setq org-structure-tempate-alist (assoc-delete-all "s" org-structure-template-alist))

  (add-to-list 'org-structure-template-alist
               '("l" .
                 "src elisp :results output :wrap example"))
  (add-to-list 'org-structure-template-alist
               '("j" .
                 "src js :results output :wrap example :cmd \"node --input-type=module < \""))
  (add-to-list 'org-structure-template-alist
               '("p" .
                 "src python :results output :wrap example"))
  (add-to-list 'org-structure-template-alist
               '("s" .
                 "src shell :results output :wrap example"))
  (add-to-list 'org-structure-template-alist
               '("r" .
                 "src rust :results output :wrap example :main no"))

  (org-tempo-add-templates)
