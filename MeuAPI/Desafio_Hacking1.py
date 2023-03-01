# Importando bibliotecas necessárias
import requests
import numexpr

# Desativando a exibição de mensagens de aviso relacionadas à conexão SSL
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# URL do desafio
url = "https://desafios.cysource.com.br/PYTHON/stage1.php"

# Função para obter o desafio do servidor
def puxar_desafio():
    # Fazendo uma requisição HTTP GET para a URL do desafio, sem verificar o certificado SSL
    r = session.get(url, stream=True, verify=False)
    # Iterando sobre as linhas da resposta do servidor
    for linha in r.iter_lines():
        # Convertendo a linha para string
        linha = str(linha)
        # Verificando se a linha contém a equação a ser resolvida
        if '<h3 class="text-center">' in str(linha):
            # Retornando somente a equação
            return linha[linha.rfind(" ") + 1:linha.find("</h3")]

# Função para resolver o desafio
def resolver_desafio(solucao):
    # URL da API para enviar a solução
    r = session.post(solucao_url, data="solution{0}=&chal=stage1".format(solucao), stream=True, headers=header, verify=False)
    # Iterando sobre as linhas da resposta do servidor
    for linha in r.iter_lines():
        # Convertendo a linha para string
        linha = str(linha)
        # Verificando se a resposta do servidor contém a mensagem de "resolvido" ou "You"
        if 'resolvido:' in linha or 'You' in linha:
            # Imprimindo a resposta do servidor
            print(linha)

# Criando uma sessão com o servidor
session = requests.session()
# Configurando o header para a requisição HTTP POST
header = {"content-type": "application/x-www-form-urlencoded"}
# URL da API para enviar a solução
solucao_url = "https://desafios.cysource.com.br/PYTHON/api.php"

# Loop para resolver o desafio seis vezes
for i in range(6):
    try:
        # Obtendo o desafio do servidor
        desafio = puxar_desafio()
        # Avaliando a expressão matemática do desafio
        solucao = numexpr.evaluate(desafio)
        # Enviando a solução para o servidor
        resolver_desafio(solucao)
    except:
        # Caso ocorra alguma exceção, passa para a próxima iteração do loop
        pass
