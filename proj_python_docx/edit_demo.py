from docx import Document

document = Document('demo.docx')

for paragraph in document.paragraphs:
    if 'Sea' in paragraph.text:
        print paragraph.text
        paragraph.text = 'new text containing ocean'
document.save('demo.docx')

