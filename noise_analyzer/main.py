# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# main.py

from analyzer_config import AnalyzerConfig
from noise_wave_analyzer import NoiseWaveAnalyzer
from receiving_data import ReceivingData


class Main:
    '''Main class. Where the magic start to happen :-)
    '''

    def __init__(self):
        '''Initialize default class values.
        '''
        self.__load_config()
        self.__define_wave_analyzer()

    def run(self):
        '''Execute the program.
        '''
        print 'Starting analyzer...'

        receiving_data = ReceivingData(analyzer=self.noise_wave_analyzer, port=self.config.port)
        receiving_data.read_and_analyze()

        print 'Analyzer finishing...'

    def __load_config(self):
        '''Load the analyzer configuration.
        '''
        analyzer_config = AnalyzerConfig()
        analyzer_config.load()
        self.config = analyzer_config

    def __define_wave_analyzer(self):
        '''Define the analyzer class that will decide if the signal is a wave or a noise.
        '''
        self.noise_wave_analyzer = NoiseWaveAnalyzer(self.config.sample_rate, self.config.noise_filename)


if __name__ == "__main__":
    main = Main()
    main.run()
