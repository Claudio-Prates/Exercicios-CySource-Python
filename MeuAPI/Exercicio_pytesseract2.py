import pytesseract
import requests

# Desativando a exibição de mensagens de aviso relacionadas à conexão SSL
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://desafios.cysource.com.br/PYTHON/"

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Cláudio Junior\AppData\Local\Tesseract-OCR\tesseract.exe'


def puxar_captcha(session):
    r = session.get(url + "stage2.php?level=0", stream=True)
    for linha in r.iter_lines():
        linha = str(linha)
        if "captcha_image" in linha:
            path_imagem = linha[linha.rfind("img"):linha.find("png") + 3]

    r = session.get(url + path_imagem)
    with open("a.png", "wb") as f:
        f.write(r.content)
    return pytesseract.image_to_string("a.png").replace("\n", "")[:-1]


def enviar_captcha(session, captcha, level):
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {"captcha": captcha, "chal": "stage2", "level": level}
    r = session.post(url + "api.php", data=data, headers=headers)
    if "You did it, time to level up" in r.text:
        return True
    else:
        return False


session = requests.session()
contador = 0

while True:
    contador += 1
    captcha = puxar_captcha(session)
    if enviar_captcha(session, captcha, level="1"):
        break

print("tentativas:", contador)
print("You did it, time to level up! Add the parameter level=1 or level=2 to continue.")
