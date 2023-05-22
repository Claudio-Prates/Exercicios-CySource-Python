import pytesseract
import requests
url = "https://desafios.cysource.com.br/PYTHON/"

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Cláudio Junior\AppData\Local\Tesseract-OCR\tesseract.exe'


def puxar_captcha():
    r = session.get(url + "stage2.php?level=0",  stream=True)
    for linha in r.iter_lines():
        linha = str(linha)
        if "captcha_image" in linha:
            path_imagem = linha[linha.rfind("img"):linha.find("png") + 3]

    r = session.get(url + path_imagem)
    with open("a.png", "wb") as f:
        f.write(r.content)
    return pytesseract.image_to_string("a.png").replace("\n", "")[:-1]



def enviar_captcha():
    headers = {"content-type":"application/x-www-form-urlencoded"}
    r = session.post(url + "api.php", data="captcha={0}&chal=stage2&level=0".format(captcha).encode('utf-8'), headers=headers)

    if "you did it" in r.text:
        print(r.text)
        return True
    else:
        return False



session = requests.session()
contador = 0

while True:
    captcha = puxar_captcha()
    contador += 1
    if enviar_captcha():
        break

print("tentativa:",contador)