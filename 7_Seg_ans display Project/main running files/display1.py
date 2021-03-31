import serial

#baudrate should match the number written in arduino ide
ser  = serial.Serial("COM6", baudrate = 9600, timeout = 1)

def clear_display():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'g')

     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'L')
     ser.write(b'M')
     ser.write(b'n')

def off():
     ser.write(b'a')
     ser.write(b'b')
     ser.write(b'c')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g')

     ser.write(b'h')
     ser.write(b'i')
     ser.write(b'j')
     ser.write(b'k')
     ser.write(b'l')
     ser.write(b'm')
     ser.write(b'n')

#-----------------------------------display 1-----------------------------------#
def minus():
     ser.write(b'a')
     ser.write(b'b')
     ser.write(b'c')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'G')

def zero():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'g')

def one():
     ser.write(b'a')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g')

def two():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'c')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'f')
     ser.write(b'G')

def three():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'G')

def four():
     ser.write(b'a')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')

def five():
     ser.write(b'A')
     ser.write(b'b')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')

def six():
     ser.write(b'A')
     ser.write(b'b')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'G')

def seven():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'd')
     ser.write(b'e')
     ser.write(b'f')
     ser.write(b'g')

def eight():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'E')
     ser.write(b'F')
     ser.write(b'G')

def nine():
     ser.write(b'A')
     ser.write(b'B')
     ser.write(b'C')
     ser.write(b'D')
     ser.write(b'e')
     ser.write(b'F')
     ser.write(b'G')

#-----------------------------------display 2-----------------------------------#

def zero_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'L')
     ser.write(b'M')
     ser.write(b'n')

def one_2():
     ser.write(b'h')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'k')
     ser.write(b'l')
     ser.write(b'm')
     ser.write(b'n')

def two_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'j')
     ser.write(b'K')
     ser.write(b'L')
     ser.write(b'm')
     ser.write(b'N')

def three_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'l')
     ser.write(b'm')
     ser.write(b'N')

def four_2():
     ser.write(b'h')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'k')
     ser.write(b'l')
     ser.write(b'M')
     ser.write(b'N')

def five_2():
     ser.write(b'H')
     ser.write(b'i')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'l')
     ser.write(b'M')
     ser.write(b'N')

def six_2():
     ser.write(b'H')
     ser.write(b'i')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'L')
     ser.write(b'M')
     ser.write(b'N')

def seven_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'k')
     ser.write(b'l')
     ser.write(b'm')
     ser.write(b'n')

def eight_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'L')
     ser.write(b'M')
     ser.write(b'N')

def nine_2():
     ser.write(b'H')
     ser.write(b'I')
     ser.write(b'J')
     ser.write(b'K')
     ser.write(b'l')
     ser.write(b'M')
     ser.write(b'N')