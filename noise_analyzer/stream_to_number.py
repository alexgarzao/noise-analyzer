# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# stream_to_number.py

class StreamToNumber:
	def __init__(self):
		self.values = []
		self.buffer = ''

	def ProcessStream(self, streamData):
		streamData = self.buffer + streamData
		self.buffer = ''
		for c in streamData:
			if c == '\n' or c == '\r':
				if self.buffer != '':
					self.values.append(int(self.buffer))
					self.buffer = ''
			else:
				self.buffer += c
		return self.buffer

	def GetNumericalValues(self):
		result = self.values[:]
		self.values = []
		return result

	def Size(self):
		return len(self.values)
