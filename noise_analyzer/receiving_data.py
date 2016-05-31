# -*- encoding: utf-8 -*-
# Noise wave analyzer
# Author: Alex S. Garzão <alexgarzao@gmail.com>
# receiving_data.py

import socket

from stream_to_number import StreamToNumber


class ReceivingData:
    '''Responsible for accept connections, read the data and send to the defined analyzer.
    '''

    def __init__(self, analyzer, port):
        '''Initialize the object.

        analyzer: define the analyzer (class) responsible for analyze the data stream and tell if is a wave (or noise) signal.
        port: port where the analyzer will accept connections.
        '''
        self.analyzer = analyzer
        self.port = port

    def read_and_analyze(self):
        '''Read the stream data, parser into numerical values, and send to the analyzer class.
        '''
        print 'Reading at port %s' % self.port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))        # Available in all interfaces.
        s.listen(1)

        while True:
            conn, addr = s.accept()

            self.__process_new_connection(conn)

            conn.close()

    def __process_new_connection(self, conn):
        '''Process the stream data that are comming in a connection.

        conn: connection.
        '''
        print 'Connection received...'

        stream_parser = StreamToNumber()

        while 1:
            data = conn.recv(1024)
            if not data:
                break

            stream_parser.process_stream(data)
            if stream_parser.size() > 0:
                self.analyzer.process_values(stream_parser.get_numerical_values())

        self.analyzer.sample_finished()
