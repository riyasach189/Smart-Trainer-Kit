#from gate_tester import *
#print(gatetester("CD4001"))

from machine import Pin
from time import sleep

p1 = Pin(2,Pin.OUT)
p2 = Pin(3,Pin.OUT)
p3 = Pin(4,Pin.IN)
g = Pin(8,Pin.OUT)
g.value(0)

lst = [
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,1,0]
    ]


for i in lst:
    newlst = ""
    p1.value(i[0])
    p2.value(i[1])
    sleep(0.05)
    if p3.value() == i[2]:
        print(True)
    else:
        print(False)