"""Pentester lab bootcamp 
week 2 - http client with sockets
James Dolan
"""
import sys
import socket


def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
		print('failed ot create socket, error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
		sys.exit()
	print('socket created\n')
	try:
		host = '127.0.0.1'
	except socket.gaierror:
		print('host failed\n')
	port = 80

	s.connect((host, port))
	print('connected\n')

	message = b"GET / HTTP/1.0\r\n\r\n"
	try:
		s.sendall(message)
	except socket.error:
		print('send failed\n' + str(msg[0]) + ' \n Error message : ' + msg[1])
		sys.exit()

	print(s.recv(4096))

	s.close

if __name__=='__main__':
	main()
