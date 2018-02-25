#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received: ')
		request = str(recvSocket.recv(1024), 'utf-8')
		print(request)
		resource = request.split()[1]
		print("Resource: ", resource)
		_, num1, op, num2 = resource.split('/')
		print(num1, op, num2)
		result = str(calculadora.calcular(num1, num2, op))
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>El resultado es: " + result + "</html></body></h1>","utf-8"))
		recvSocket.close()

except KeyboardInterrupt:
	print("Closing...")
mySocket.close()

