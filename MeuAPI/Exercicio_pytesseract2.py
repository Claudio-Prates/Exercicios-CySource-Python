import pytesseract
import requests

# Desativando a exibição de mensagens de aviso relacionadas à conexão SSL
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import pytesseract
import requests

# URL do desafio
url = "https://desafios.cysource.com.br/PYTHON/"

# Caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Cláudio Junior\AppData\Local\Tesseract-OCR\tesseract.exe'


def puxar_captcha(session):
    # Faz uma requisição GET para obter o código HTML da página
    r = session.get(url + "stage2.php?level=0", stream=True)
    
    # Procura pela linha que contém a imagem do captcha
    for linha in r.iter_lines():
        linha = str(linha)
        if "captcha_image" in linha:
            path_imagem = linha[linha.rfind("img"):linha.find("png") + 3]

    # Faz uma requisição GET para obter a imagem do captcha
    r = session.get(url + path_imagem)
    
    # Salva a imagem em um arquivo local chamado "a.png"
    with open("a.png", "wb") as f:
        f.write(r.content)
    
    # Utiliza o Tesseract OCR para extrair o texto do captcha
    return pytesseract.image_to_string("a.png").replace("\n", "")[:-1]


def enviar_captcha(session, captcha, level):
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {"captcha": captcha, "chal": "stage2", "level": level}
    
    # Envia uma requisição POST para submeter o captcha
    r = session.post(url + "api.php", data=data, headers=headers)
    
    # Verifica se a resposta indica sucesso
    if "You did it, time to level up" in r.text:
        return True
    else:
        return False


# Cria uma sessão HTTP para manter o estado da conexão
session = requests.session()

# Contador de tentativas
contador = 0

while True:
    contador += 1
    
    # Obtém o captcha
    captcha = puxar_captcha(session)
    
    # Envia o captcha e verifica se foi aceito
    if enviar_captcha(session, captcha, level="1"):
        break

# Imprime o número de tentativas
print("tentativas:", contador)

# Imprime a mensagem de sucesso
print("You did it, time to level up! Add the parameter level=1 or level=2 to continue.")

