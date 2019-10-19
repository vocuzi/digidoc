import serial
import os, time
 
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.01)
 
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
 
fd=''
while True:
    rcv = port.read(10)
    if len(rcv) &gt; 1:
        fd=fd+rcv
        ps=fd.find('\r')
        if ps &gt;= 0:
            print fd[0:ps]
            fd=''