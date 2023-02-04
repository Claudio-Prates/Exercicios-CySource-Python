import random

from flask import Flask, session, jsonify, request
from random import randint

# Inicialização da aplicação Flask com o nome "Servidor API da ITsafe"
app = Flask("Servidor API da ITsafe", static_url_path='')

# Definição da chave secreta da sessão
app.secret_key = 'ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd'

# Rota "/comecar_jogo" para iniciar o jogo
@app.route('/comecar_jogo', methods=['GET'])
def comecar_jogo():
    # Gera um número aleatório entre 1 e 100 e salva na sessão
    session["numero"] = random.randint(1, 100)

    # Retorna um objeto JSON indicando que o jogo foi iniciado com sucesso
    return jsonify({"success": True})

# Rota "/adivinhar_numero" para fazer uma tentativa de adivinhação
@app.route('/adivinhar_numero', methods=['POST'])
def adivinhar_numero():
    # Variável "status" é definida como "maior"
    status = "maior"

    # Imprime os dados da solicitação JSON
    print(request.json)

    # Retorna um objeto JSON com o status da tentativa de adivinhação
    return jsonify({"status": status})

# Habilita a opção de depuração
debug = True

# Inicia a aplicação com o host '0.0.0.0' na porta 1337
app.run(host='0.0.0.0', port=1337, debug=debug)
