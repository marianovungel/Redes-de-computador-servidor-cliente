from socket import *
import os
serverPort = 12075

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('servidor pronto para receber pedidos!')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    os.chdir('static')
    connectionSocket.send(os.chdir('static'))
    connectionSocket.close()