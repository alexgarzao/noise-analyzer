# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# main.py

import argparse

from noise_wave_analyzer import NoiseWaveAnalyzer
from receiving_data import ReceivingData


class Main:
    '''Main class. Where the magic start to happen :-)
    '''

    def run(self):
        '''Execute the program.
        '''
        print 'Starting analyzer...'

        self.__parser_args()

        self.__define_wave_analyzer()

        receiving_data = ReceivingData(analyzer=self.noise_wave_analyzer, port=self.args.port)
        receiving_data.read_and_analyze()

        print 'Analyzer finishing...'

    def __define_wave_analyzer(self):
        '''Define the analyzer class that will decide if the signal is a wave or a noise.
        '''
        self.noise_wave_analyzer = NoiseWaveAnalyzer(self.args.sample_rate, self.args.noise_filename)

    def __parser_args(self):
        '''Define the analyzer configuration.
        '''
        parser = argparse.ArgumentParser(description = 'Identify noise signal in a sample.')

        parser.add_argument(
                    '--sample-rate',
                    dest='sample_rate',
                    action='store',
                    type=int,
                    default=50,
                    help='Sample rate in the stream (default=50)'
        )

        parser.add_argument(
                    '--port',
                    dest='port',
                    action='store',
                    type=int,
                    default=55678,
                    help='Port where the analyzer will attend requests (default=55678)'
        )

        parser.add_argument(
                    '--noise-filename',
                    dest='noise_filename',
                    action='store',
                    type=str,
                    default='noise_connection_',
                    help='Base filename where the noise will be saved (default="noise_connection_")'
        )

        self.args = parser.parse_args()

        print 'Configuration'
        print '\tSample rate: %d' % self.args.sample_rate
        print '\tPort: %d' % self.args.port
        print '\tNoise base filename: %s' % self.args.noise_filename


if __name__ == "__main__":
    main = Main()
    main.run()
