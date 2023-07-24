#CD4071

from machine import *
from utime import *

p1 = Pin(16,Pin.OUT)
p2 = Pin(17,Pin.OUT)
p3 = Pin(18,Pin.IN)
p4 = Pin(19,Pin.IN)
p5 = Pin(20,Pin.OUT) 
p6 = Pin(21,Pin.OUT)
p7 = Pin(22,Pin.OUT)
#p8_GND 
p9 = Pin(2, Pin.OUT)
p10 = Pin(3, Pin.OUT)
p11 = Pin(4,Pin.OUT)
p12 = Pin(5,Pin.IN)
p13 = Pin(6,Pin.IN)
p14 = Pin(7,Pin.OUT)
p15 = Pin(8,Pin.OUT)
#p16_Vcc

p7.off()
p9.off()


lst = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]
    ]

print("Gate 1: ")
for i in lst:
    p1.value(i[0])
    p2.value(i[1])
    sleep(0.05)
    print(p3.value() == i[2])

print("Gate 2: ")
for i in lst:
    p5.value(i[0])
    p6.value(i[1])
    sleep(0.05)
    print(p4.value() == i[2])

print("Gate 3: ")
for i in lst:
    p10.value(i[0])
    p11.value(i[1])
    sleep(0.05)
    print(p12.value() == i[2])

print("Gate 4: ")
for i in lst:
    p14.value(i[0])
    p15.value(i[1])
    sleep(0.05)
    print(p13.value() == i[2])
