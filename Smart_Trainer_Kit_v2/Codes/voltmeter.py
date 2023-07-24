'''
PICO has ADC channels
    PIN31 = GP26 = ADC0
    PIN32 = GP27 = ADC1
    PIN38 = GP28 = ADC2
    Internal Temp Sensor = ADC3
    
    ADC is a 12 bit resolution internal to the RP2040 meaning a range of 0 ~ 4095
    ADC value from Micropython is 16 bits meaning a range of 0 ~ 65535
    Micropython maps the 12 bit range to 16 bits for ease of use on various micros
'''

import machine
import utime
from pico_i2c_lcd import I2cLcd
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

pot_val = machine.ADC(0)
conversion_factor = 5/65535

while True:
    reading = pot_val.read_u16()
    data = round(reading * conversion_factor,2)
    lcd.putstr(str(data))
    utime.sleep(0.1)
    lcd.clear()