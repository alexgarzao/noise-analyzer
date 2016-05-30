# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# NoiseWaveAnalyzer.py


class NoiseWaveAnalyzer:
	'''NoiseWaveAnalyzer receives a threshold and, based on this value, can decide if the data is a good signal or a noise.
	'''

	def __init__(self, threshold, noise_filename=None):
		'''Initialize the object.

		threshold: is the limit to decide if a data is a wave or a noise.
		noise_filename: is the csv to be generated with the noise.
		'''
		if noise_filename != None:
			self.noise_file = open(noise_filename,'a')
		else:
			self.noise_file = None
		self.Threshold = threshold

	def IsNoise(self, value):
		'''Verifiy if the value is a noise.

		value: data to be analyzed.
		'''
		return value <= self.Threshold


	def ProcessValues(self, data):
		'''Process values in data to known if its a noise.

		data - list with the numerical values to be analyzed.
		'''
		for value in data:
			if not self.IsNoise(value):
				continue

			print "Noise: %s" % value

			if self.noise_file != None:
				self.noise_file.write(str(value) + '\n')
