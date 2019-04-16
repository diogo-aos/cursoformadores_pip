import pdftools as pt
import os

pip_n_pages = 15

pip = '/home/chiro/workspace/CursoFormadores/PIP/pip.pdf'
to_insert = {1: (14,'/home/chiro/workspace/CursoFormadores/PIP/observacao.pdf'),
             2: (15,'/home/chiro/workspace/CursoFormadores/PIP/aval_formativa.pdf'),
             3: (16,'/home/chiro/workspace/CursoFormadores/PIP/questionario_satisfacao.pdf')}
to_rotate = [1,3]

# rotate 




pt.pdf_insert(pip, a3, None, 16)
pt.pdf_insert(pip, a2, None, 15)
pt.pdf_insert(pip, a1, None, 14)
