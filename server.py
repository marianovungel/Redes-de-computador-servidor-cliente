
#importações
from socket import *
import os

#criação da  porta do servidor
serverPort = 12075

#Estabelecer a conexão com o método TCP (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)

#passar a porta de conexão com o servidor
serverSocket.bind(('', serverPort))

#o servidor a espera de uma mensagem do cliente
serverSocket.listen(1)

print('servidor pronto para receber pedidos!')

while 1:
    #aceitar a conexão com o cliente
    connectionSocket, addr = serverSocket.accept()
    
    #validar a quantidade de bits a receber
    sentence = connectionSocket.recv(1024)

    #fazer o envio do arquivo html
    connectionSocket.send(os.chdir('static'))

    #feixar a conexão do servidor
    connectionSocket.close()