'''
Loop through the directory,
    for each one, merge the image files into one pdf and add a bookmark with the directory's name (reference number)
'''
import img2pdf
from PIL import Image
import os
import glob

WORKING_DIR = ''

def convert_img_to_pdf(img_path, pdf_path):
    image = Image.open(img_path)

    # Convert to pdf bytes
    pdf_bytes = img2pdf.convert([img_path])
    
    file = open(pdf_path, 'wb')
    file.write(pdf_bytes)
    
    image.close()
    file.close()
    print('pdf created')

def find_all_images(working_dir, exts):
    img_paths = []
    for ext in exts:
        img_paths += glob.glob(f'**/*.{ext}', recursive=True)
    return img_paths

def remove_alpha_channel(img_paths):
    for img in img_paths:
        base_path, _ = os.path.split(img)
        name_without_ext = os.path.splitext(img)[0]
        os.system(f'convert {img} -background white -alpha remove -alpha off {base_path}/converted_{name_without_ext}.jpg')

if __name__ == '__main__':
    img_path = '/Users/vincenthuang/Development/output.png'
    pdf_path = '/Users/vincenthuang/Development/test.pdf'
    convert_img_to_pdf(img_path, pdf_path)

    