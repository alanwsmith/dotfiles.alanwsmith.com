(require 'org-tempo)

(setq org-structure-tempate-alist (assoc-delete-all "l" org-structure-template-alist))
(setq org-structure-tempate-alist (assoc-delete-all "s" org-structure-template-alist))

(add-to-list 'org-structure-template-alist
             '("l" .
               "src elisp :results output :wrap example :post padder(data=*this*)"))
(add-to-list 'org-structure-template-alist
             '("j" .
               "src js :results output :wrap example :post padder(data=*this*) :cmd \"node --input-type=module < \""))
(add-to-list 'org-structure-template-alist
             '("p" .
               "src python :results output :wrap example :post padder(data=*this*)"))
(add-to-list 'org-structure-template-alist
             '("r" .
               "src ruby :results output :wrap example :post padder(data=*this*)"))
(add-to-list 'org-structure-template-alist
             '("s" .
               "src shell :results output :wrap example :post padder(data=*this*)"))


(org-tempo-add-templates)
