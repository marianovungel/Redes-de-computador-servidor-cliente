#fazer a importação
from socket import *

#noma do IP (Local)
serverName = '127.0.0.1'

#criar porta
serverPort = 12075

#Estabelecer a conexão com o método TCP (SOCK_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#digite a porta para se conectar
sentence = input('Digite a porta para se conectar: ').encode('utf-8')

#fazer o envio da mensagem
clientSocket.send(sentence)
modifedSentence = clientSocket.recv(2048)

#resposta do servidor
print(('do Servidor: '), modifedSentence.decode('utf-8'))

#feixar a conexão do cliente
clientSocket.close()