from pio_clock import *
from machine import *
import utime
from rotary_encoder_classes import *
from constants import *
from pico_i2c_lcd import I2cLcd
from gate_tester import *
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

#clocks
sm_1.active(1)
sm_5.active(1)
sm_10.active(1)

#gate tester
ic_tester_screen = 0
ic_selected = ""

#voltmeter
pot_val = machine.ADC(0)
conversion_factor = 5/65535

#lcd
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

#rotary encoder
last_Enc_Counter_1 = 0
Enc_Counter_1 = 0
Last_Qtr_Cntr_1 = 0
Qtr_Cntr_1 = 0
error_1 = 0

Enc_1 = R_Encoder(15, 14)
Enc_1.DisplayPins()
Enc_1.Reset_Counter()

Enc_1_SW = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
Enc_1_SW_State = "UP"

#main menu
pointer = 0
ic_menu_pointer = -1
main_menu_options = ["> IC Tester", "> Voltmeter"]
ic_options = len(ic_tester_options)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr(main_menu_options[pointer])