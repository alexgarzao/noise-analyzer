# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# receiving_data.py


import socket


class ReceivingData:
	'''Responsible for accept connections, read the data and send to the defined analyzer.
	'''


	def __init__(self, analyzer, port):
		'''Initialize the object.

		analyzer: define the analyzer (class) responsible for analyze the data stream and tell if is a wave (or noise) signal.
		port: port where the analyzer will accept connections.
		'''
		self.Analyzer = analyzer 
		self.Port = port


	def ReadAndAnalyze(self):
		print 'Reading at port %s' % self.Port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('', self.Port)) # Available in all interfaces.
		s.listen(1)
		while True:
			conn, addr = s.accept()
#			print 'Connected by', addr
			while 1:
				data = conn.recv(1024)
				if not data: break
				conn.sendall(data)
				print 'data reived: %s' % data
			conn.close()
