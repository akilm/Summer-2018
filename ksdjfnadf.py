import serial
ser=serial.Serial('COM5',9600)
rpm1=ser.read(1);
rpm2=ser.read(2);
print(rpm1);
print(rpm2);
