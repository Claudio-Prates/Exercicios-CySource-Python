# Importa as bibliotecas requests e json
import requests
import json

# Inicia uma sessão com o servidor
session = requests.session()

# Cria um dicionário com a chave "palpite" inicializada com 0
dados = {"palpite": 0}

# Define o cabeçalho da solicitação com "content-type" como "application/json"
header = {"content-type": "application/json"}

# Realiza a primeira solicitação HTTP GET ao endpoint "http://127.0.0.1:1337/comecar_jogo"
r = session.get("http://127.0.0.1:1337/comecar_jogo")

# Verifica se a resposta contém "success" com o valor True
if r.json()["success"]:
    # Se sim, inicia um loop infinito
    while True:
        # Solicita ao usuário um palpite
        dados["palpite"] = input('Adivinhe o número > ')

        # Realiza uma solicitação HTTP POST ao endpoint "http://127.0.0.1:1337/adivinhar_numero"
        # com o corpo da mensagem contendo os dados codificados em JSON e o cabeçalho definido
        r = session.post("http://127.0.0.1:1337/adivinhar_numero", data=json.dumps(dados), headers=header)

        # Armazena a resposta em formato JSON na variável meu_json
        meu_json = r.json()

        # Imprime a resposta
        print(meu_json)

        # Verifica se a resposta contém "status" com o valor "vc acertou"
        if meu_json["status"] == "vc acertou":
            # Se sim, interrompe o loop e o jogo termina
            break
else:
    # Se a resposta da primeira solicitação não contém "success" com o valor True,
    # imprime a mensagem "Sem permissão para jogar" e o jogo não começa
    print('Sem permissão para jogar')
