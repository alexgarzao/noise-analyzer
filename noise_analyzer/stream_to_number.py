# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# stream_to_number.py


class StreamToNumber:
    '''Responsible to parser a stream of values to extract the numerical values.
    '''

    def __init__(self):
        '''Init method.
        '''
        self.values = []
        self.buffer = ''

    def process_stream(self, stream_data):
        '''Process the stream to extract the numerical values.

        stream_data: stream to be processed.
        '''
        stream_data = self.buffer + stream_data
        self.buffer = ''
        for c in stream_data:
            if c < '0' or c > '9':
                if self.buffer != '':
                    self.values.append(int(self.buffer))
                    self.buffer = ''
            else:
                self.buffer += c
        return self.buffer

    def get_numerical_values(self):
        '''Return the numerical values parsed from the stream.

        The values are returned and are cleaned from here.
        '''
        result = self.values[:]
        self.values = []
        return result

    def size(self):
        '''Return the number of numerical values parsed.
        '''
        return len(self.values)
