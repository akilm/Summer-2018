import serial
s = serial.Serial('COM5',9600)
s.flushInput()
while(1):
    a = ord(s.read())
    b = ord(s.read())
    c = print( a|(b<<8))
