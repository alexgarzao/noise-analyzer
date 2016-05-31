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


    def ProcessStream(self, streamData):
        '''Process the stream to extract the numerical values.
        '''
        streamData = self.buffer + streamData
        self.buffer = ''
        for c in streamData:
            if c == '\n' or c == '\r' == ' ':
                if self.buffer != '':
                    self.values.append(int(self.buffer))
                    self.buffer = ''
            else:
                self.buffer += c
        return self.buffer


    def GetNumericalValues(self):
        '''Return the numerical values parsed from the stream.

        The values are returned and are cleaned from here.
        '''
        result = self.values[:]
        self.values = []
        return result

    def Size(self):
        '''Return the number of numerical values parsed.
        '''
        return len(self.values)
