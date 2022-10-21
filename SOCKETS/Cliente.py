from socket import *

cliente = socket(AF_INET,SOCK_STREAM) #blablabla Familia de endereços Ipv4 (AF_INET, SOCK_STREAM) TCP,ou UDP (socket(AF_INET, SOCK_DGRAM)
cliente.connect(("192.168.0.2",4444)) # Clientes querendo se conectar


while True:
    # Cliente envia os dados para o Servidor
    dados = input('Cliente:')
    cliente.sendall(dados.encode()) # Codificando pacote binário dos Dados

    if dados == "sair": # Se o cliente decidir encerrar a conversa
        cliente.close()
        break


    # Cliente recebe os dados do Servidor
    dados = cliente.recv(2048).decode()
    print(f'Servidor {dados}')





