# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# main.py

from analyzer_config import AnalyzerConfig
from NoiseWaveAnalyzer import NoiseWaveAnalyzer

class Main:
	'''Main class. Where the magic start to happen :-)
	'''

	def __init__(self):
		'''Initialize default class values.
		'''
		self.loadConfig()
		self.defineWaveAnalyzer()


	def Run(self):
		'''Execute the program.
		'''
		print 'Starting analyzer...'

		print 'Analyzer finishing...'


	def loadConfig(self):
		'''Load the analyzer configuration.
		'''
		analyzerConfig = AnalyzerConfig()
		analyzerConfig.load()
		self.Config = analyzerConfig


	def defineWaveAnalyzer(self):
		'''Define the analyzer class that will decide if the signal is a wave or a noise.
		'''
		self.NoiseWaveAnalyzer = NoiseWaveAnalyzer(self.Config.Threshold)


if __name__ == "__main__":
    main = Main()
    main.Run()
