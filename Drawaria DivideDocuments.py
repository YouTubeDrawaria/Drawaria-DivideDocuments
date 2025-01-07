from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def divide_file(file_path, num_parts=4):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Calcular el tamaño de cada chunk
    total_chars = len(content)
    chunk_size = total_chars // num_parts

    # Dividir el contenido en chunks
    chunks = [content[i:i + chunk_size] for i in range(0, total_chars, chunk_size)]

    # Asegurarse de que no haya más chunks que el número de partes solicitado
    if len(chunks) > num_parts:
        chunks = chunks[:num_parts]

    for i, chunk in enumerate(chunks):
        pdf_file_path = f'part_{i + 1}.pdf'
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        text = c.beginText(40, 750)  # Posición inicial del texto
        text.setFont("Helvetica", 12)
        
        # Dividir el chunk en líneas para que quepa en el PDF
        lines = chunk.split('\n')
        for line in lines:
            text.textLine(line)
        
        c.drawText(text)
        c.save()

    print(f'File divided into {len(chunks)} parts.')

# Usage
divide_file('main.js', num_parts=4)
