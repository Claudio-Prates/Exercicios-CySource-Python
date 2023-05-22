import cv2
import pytesseract

# estamos lendo a imagem
img = cv2.imread("img.png")


# apontar onde está o executável do tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

config = r'--oem 3 --psm 6'
resultado = pytesseract.image_to_string(img, config=config)
print(resultado)
