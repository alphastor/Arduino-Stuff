import serial

ser = serial.Serial("COM5", baudrate=9600, timeout = 1)

def clear():
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