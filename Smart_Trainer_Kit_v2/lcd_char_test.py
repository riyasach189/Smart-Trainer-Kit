import machine
from rotary_encoder_classes import *
from constants import *
import utime
from pico_i2c_lcd import I2cLcd
from gate_tester import *
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#lcd.putstr("[ ]   [ ]   [ ]\n[ ]   [ ]   [ ]")

# lcd.putstr("  [ ]      [ ]\n  [ ]      [ ]")

lcd.putstr("      " + '[ ]' + "\n" + "      " + '[ ]')