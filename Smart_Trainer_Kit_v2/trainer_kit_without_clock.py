import machine
from rotary_encoder_classes import *
import utime
from pico_i2c_lcd import I2cLcd
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

#gate tester
ic_tester_screen = 0

#voltmeter
pot_val = machine.ADC(0)
conversion_factor = 5/65535

#clock
clock_pointer = -1
clock_options = [0.1, 1, 10]
frequency = 1
clock_led = machine.Pin(25, machine.Pin.OUT)

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
main_menu_options = ["> Clock Frequency", "> IC Tester", "> Voltmeter"]
ic_tester_options = ["> 74LS04", "> 74LS08", "> CD4001", "> CD4011", "> CD4070", "> CD4071", "> CD4077", "> CD4081", "> 74LS153", "> CD4013B", "> SN74LS157"]
ic_options = len(ic_tester_options)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr(main_menu_options[pointer])

#Main Program
while True:
    #clock_led.toggle()
    #utime.sleep(1/(2*frequency))
    
    #scrolling
    Qtr_Cntr_1 = round(Enc_1.Enc_Counter/4)
    if Qtr_Cntr_1 != Last_Qtr_Cntr_1:
        print(Qtr_Cntr_1)
        
        if (pointer >= 0):
            
            if (Qtr_Cntr_1 > Last_Qtr_Cntr_1):
                pointer = (pointer + 1)%3
                
            else:
                pointer = (pointer - 1)%3
            
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])
            
        elif (ic_menu_pointer >= 0):
            
            if (Qtr_Cntr_1 > Last_Qtr_Cntr_1):
                ic_menu_pointer = (ic_menu_pointer + 1)%ic_options
                
            else:
                ic_menu_pointer = (ic_menu_pointer - 1)%ic_options
            
            lcd.clear()
            lcd.putstr(ic_tester_options[ic_menu_pointer])
            
        elif (clock_pointer >= 0):
            if (Qtr_Cntr_1 > Last_Qtr_Cntr_1):
                clock_pointer = (clock_pointer + 1)%3
                
            else:
                clock_pointer = (clock_pointer - 1)%3
            
            lcd.clear()
            lcd.putstr("> " + str(clock_options[clock_pointer]))
            
        last_Enc_Counter_1 = Enc_1.Enc_Counter
        Last_Qtr_Cntr_1 = Qtr_Cntr_1
        
    #clicking
    if (Enc_1_SW.value() == True) and (Enc_1_SW_State == "DOWN"):
        Enc_1_SW_State = "UP"
        print("Switch is UP")
    elif (Enc_1_SW.value() == False) and (Enc_1_SW_State == "UP"):
        Enc_1_SW_State = "DOWN"
        print("Switch is DOWN")
        if (pointer == 1):
            pointer = -1
            lcd.clear()
            ic_menu_pointer = 0
            lcd.putstr(ic_tester_options[ic_menu_pointer])
            
        elif (pointer == -1):
            ic_tester_screen = 1
            pointer = -5
            ic_menu_pointer = -1
            lcd.clear()
            lcd.putstr("IC Tester Screen")
            
        elif (pointer == -5):
            ic_tester_screen = 0
            pointer = 0
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])
            
        elif (pointer == 0):
            pointer = -3
            clock_pointer = 0
            lcd.clear()
            lcd.putstr("> " + str(clock_options[clock_pointer]))
            
        elif (pointer == -3):
            frequency = clock_options[clock_pointer]
            print("Frequency: " + str(frequency))         
            pointer = 0
            clock_pointer = -1
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])
            
        elif (pointer == 2):
            Enc_1_SW_State = "UP"
            pointer = -2
            for i in range(10000):
                lcd.clear()
                reading = pot_val.read_u16()
                data = round(reading * conversion_factor, 2)
                lcd.putstr(str(data))
                utime.sleep(0.5)
                if (Enc_1_SW.value() == False) and (Enc_1_SW_State == "UP"):
                    break
                
                   
        elif (pointer == -2):
            pointer = 0
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])
