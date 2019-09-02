def bit_manipulation(a):
    a=((a & 0x0F)<<4 | (a & 0xF0)>>4)
    a=a^0xff;
    return a

def encrypt(b):
    if b<=255 :
        b=bit_manipulation(b)
    elif b<=65535:
        byte1 = b & 0x00FF
        byte2 = b & 0xFF00
        byte1 = bit_manipulation(byte1)
        byte2 = bit_manipulation(byte2)
        b = byte1 | (byte2<<8)
    elif b<=16711680:
        byte1 = b & 0x0000FF
        byte2 = b & 0x00FF00
        byte3 = b & 0xFF0000
        byte1 = bit_manipulation(byte1)
        byte2 = bit_manipulation(byte2)
        byte3 = bit_manipulation(byte3)
        b = byte1 | (byte2<<8) | (byte3<<16)

    return b

def selectionsort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j      
        A[i], A[min_idx] = A[min_idx], A[i]

    print(A)

    return A

def main():
    import csv
    import sys
    t=list()
    with open('D:\csvexample3.csv') as f:
            mycsv = csv.reader(f,delimiter=',')
            t=next(mycsv)
    for i in range(len(t)):
        t[i]=int(t[i])
    t = selectionsort(t)
    with open("D:\sorted.csv", "a") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(t)
    print('\n')
    for i in range(len(t)):
        t[i]=encrypt(t[i])
        print(t[i])
    with open("D:\encrypt.csv", "a") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(t)

if __name__== "__main__":
    main()
