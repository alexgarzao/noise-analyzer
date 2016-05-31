import socket
import sys

from lettuce import *

@step('I have the file "(.*)"')
def have_the_file(step, filename):
    world.filename = filename + '.csv'

@step('I send this file to analyzer')
def send_this_file_to_analyzer(step):
    s = socket.socket()
    s.connect(("localhost",55678))

    sample_list = [line.strip() for line in open(world.filename, 'rb').read().splitlines()]

    for sample in sample_list:
        s.send(sample + '\n')
    s.close()

@step('I see noise values equals to file "(.*)"')
def see_noise_values_equals_to_file(step, filename):
    pass

def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)

