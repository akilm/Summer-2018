import serial
import csv
import matplotlib.pyplot as plt
with open('D:\analogdata') as f:
    data = csv.reader(f,delimiter=',')
x=next(data)
y=list(range(0,10000,20))
plt.plot(x,y)
plt.xlabel(' time (ms) ')
plt.ylabel(' voltage (V) ')
plt.title(' Voltage vs time graph ')
plt.show()
