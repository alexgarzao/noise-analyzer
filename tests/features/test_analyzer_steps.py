import socket
import sys
import time

import filecmp

from lettuce import *


@step('I have the file "(.*)"')
def have_the_file(step, filename):
    world.filename = filename


@step('I send this file to analyzer')
def send_this_file_to_analyzer(step):
    send_file_to_server(host="localhost", port=55678, filename=world.filename)


@step('I see noise values in file "(.*)" equals to file "(.*)"')
def see_noise_values_equals_to_file(step, noise_filename, expected_noise_filename):
    # need time to file be flushed :-)
    time.sleep(5)

    assert filecmp.cmp(noise_filename, expected_noise_filename) is True, \
        "Noise file %s differ from expected file %s" % (noise_filename, expected_noise_filename)


# -- Support routines --


def send_file_to_server(host, port, filename):
    '''Send a file to a server.

    host - hostname where the server is running
    port - port where the service is running
    filename - file to be sent
    '''
    s = socket.socket()
    s.connect((host, port))

    with open(filename, "rb") as f:
        l = f.read(1024)
        while (l):
            s.send(l)
            l = f.read(1024)

    s.close()
