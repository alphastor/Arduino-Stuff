from pyfirmata import *
# from serial import *

matrix = Arduino("COM6")
pin = matrix.get_pin('a:0:i')
