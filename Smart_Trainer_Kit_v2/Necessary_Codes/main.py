#Main Program
while True:

    #scrolling
    Qtr_Cntr_1 = round(Enc_1.Enc_Counter/4)
    if Qtr_Cntr_1 != Last_Qtr_Cntr_1:
        print(Qtr_Cntr_1)

        if (pointer >= 0):

            if (Qtr_Cntr_1 > Last_Qtr_Cntr_1):
                pointer = (pointer + 1)%2

            else:
                pointer = (pointer - 1)%2

            lcd.clear()
            lcd.putstr(main_menu_options[pointer])

        elif (ic_menu_pointer >= 0):

            if (Qtr_Cntr_1 > Last_Qtr_Cntr_1):
                ic_menu_pointer = (ic_menu_pointer + 1)%ic_options

            else:
                ic_menu_pointer = (ic_menu_pointer - 1)%ic_options

            lcd.clear()
            lcd.putstr("> " + ic_tester_options[ic_menu_pointer])

        last_Enc_Counter_1 = Enc_1.Enc_Counter
        Last_Qtr_Cntr_1 = Qtr_Cntr_1

    #clicking
    if (Enc_1_SW.value() == True) and (Enc_1_SW_State == "DOWN"):
        Enc_1_SW_State = "UP"
        print("Switch is UP")
    elif (Enc_1_SW.value() == False) and (Enc_1_SW_State == "UP"):
        Enc_1_SW_State = "DOWN"
        print("Switch is DOWN")
        if (pointer == 0):
            pointer = -1
            lcd.clear()
            ic_menu_pointer = 0
            lcd.putstr("> " + ic_tester_options[ic_menu_pointer])

        elif (pointer == -1):
            ic_tester_screen = 1
            ic_selected = ic_tester_options[ic_menu_pointer]
            pointer = -5
            ic_menu_pointer = -1
            lcd.clear()
            gates_not_working = gatetester(ic_selected)
            total_gates = 0
            
            if icindextocategory[ics[ic_selected]] == 0:
                total_gates = 6
                output = ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
                
                for i in gates_not_working:
                    output[i] = '[!]'
                    
                lcd.putstr(output[5] + "   " + output[4] + "   " + output[3] + "\n" + output[0] + "   " + output[1] + "   " + output[2])
                
            elif ((icindextocategory[ics[ic_selected]]) in {1, 2, 3}):
                total_gates = 4
                output = ['[ ]', '[ ]', '[ ]', '[ ]']
                
                for i in gates_not_working:
                    output[i] = '[!]'
                    
                lcd.putstr("  " + output[3] + "      " + output[2] + "\n" + "  " + output[0] + "      " + output[1])
                
            elif icindextocategory[ics[ic_selected]] in {4, 5}:
                total_gates = 2
                output = ['[ ]', '[ ]']
                
                for i in gates_not_working:
                    output[i] = '[!]'
                    
                lcd.putstr("      " + output[1] + "\n" + "      " + output[0])
                
        elif (pointer == -5):
            ic_tester_screen = 0
            pointer = 0
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])

        elif (pointer == 1):
            Enc_1_SW_State = "UP"
            pointer = -2
            for i in range(10000):
                lcd.clear()
                reading = pot_val.read_u16()
                data = round(reading * conversion_factor, 2)
                lcd.putstr(str(data))
                utime.sleep(0.2)
                if (Enc_1_SW.value() == False) and (Enc_1_SW_State == "UP"):
                    break

        elif (pointer == -2):
            pointer = 0
            lcd.clear()
            lcd.putstr(main_menu_options[pointer])

