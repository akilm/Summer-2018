import serial
import csv
def main():
    s = serial.Serial('COM4',9600)
    x=list()
    i=1
    while(i<=500):
        h = ord(s.read(1)
        l = ord(s.read(1)
        d = h*100+l;         
        x.append(d)
        ++i
    with open("D:\data.csv", "a") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(x)
if __name__== "__main__":
    main()
           
    
