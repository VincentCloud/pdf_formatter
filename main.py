'''
Loop through the directory,
    for each one, merge the image files into one pdf and add a bookmark with the directory's name (reference number)
'''
import img2pdf
from PIL import Image
import os

WORKING_DIR = ''

def convert_img_to_pdf(img_path: str, pdf_path: str) -> None:
    image = Image.open(img_path)

    # Convert to pdf bytes
    pdf_bytes = img2pdf.convert([img_path])
    
    file = open(pdf_path, 'wb')
    file.write(pdf_bytes)
    
    image.close()
    file.close()
    print('pdf created')

if __name__ == '__main__':
    img_path = '/Users/vincenthuang/Development/output.png'
    pdf_path = '/Users/vincenthuang/Development/test.pdf'
    convert_img_to_pdf(img_path, pdf_path)

    