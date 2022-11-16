from socket import *
serverName = '127.0.0.1'
serverPort = 12075

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('digite a sua pesquisa: ').encode('utf-8')

clientSocket.send(sentence)
modifedSentence = clientSocket.recv(2048)

print(('do Servidor: '), modifedSentence.decode('utf-8'))

clientSocket.close()