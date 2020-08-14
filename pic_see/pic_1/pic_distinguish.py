import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'D:\\learning_file\\Tesseract-OCR\\tesseract.exe'

# lang = 'eng' 英文
text = pytesseract.image_to_string(Image.open('D:\\learning_file\\1.png'),lang='chi_sim')
print(text)
