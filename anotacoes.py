
# email windsney@gmail.com
# In......@

# aula da hastag  parou 10:50completo F669/186  c.


from docx import Document
from docx.shared import Pt, Cm

# Criação do documento
doc = Document()

# Adiciona um parágrafo com o texto desejado
paragrafo = doc.add_paragraph()
run = paragrafo.add_run("Este é um texto em itálico e com recfdfdfjdflkdjfkdjflkdjflkdsjfldkfjdlskfjdslkfjdlfjdslfjdlfjdslfjlkjdfjdslfjdslkfjdslkfsdjflkjflksdfjdskfjdlfjkdlfjdskfjdflkjsdfklsdjflsdkfjsdklfjslkuo até o meio da página.")
run.italic = True

# Define o recuo do parágrafo até o meio da página (assumindo uma largura de página padrão de 21 cm)
# Metade da página seria 10.5 cm
paragrafo.paragraph_format.left_indent = Cm(3.5)

# Salva o documento
doc.save("final.docx")