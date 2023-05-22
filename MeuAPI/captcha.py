import pytesseract
from PIL import Image

# definir uma lista com os nomes dos arquivos das imagens
nomes_arquivos = ['captcha.png', 'captcha2.png', 'captcha3.png']

# iterar sobre a lista com um loop for
for nome_arquivo in nomes_arquivos:
    # abrir o arquivo de imagem
    img = Image.open(nome_arquivo)

    # converter a imagem para escala de cinza
    img = img.convert('L')

    # utilizar o Tesseract OCR para reconhecer o texto da imagem
    texto = pytesseract.image_to_string(img)

    # exibir o texto obtido
    print(f"Texto da imagem {nome_arquivo}: {texto}")
