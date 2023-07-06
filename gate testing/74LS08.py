# and
# vcc iio iio
# iio iio gnd

def and_74LS08():
    import machine

    dip_2 = machine.Pin(4, Pin.OUT)
    dip_3 = machine.Pin(5, Pin.OUT)
    dip_4 = machine.Pin(6, Pin.IN)

    dip_5 = machine.Pin(7, Pin.OUT)
    dip_6 = machine.Pin(9, Pin.OUT)
    dip_7 = machine.Pin(10, Pin.IN)

    dip_9 = machine.Pin(11, Pin.OUT)
    dip_10 = machine.Pin(12, Pin.OUT)
    dip_11 = machine.Pin(24, Pin.IN)

    dip_12 = machine.Pin(25, Pin.OUT)
    dip_13 = machine.Pin(26, Pin.OUT)
    dip_14 = machine.Pin(27, Pin.IN)

    flags = [1,1,
            1,1]

    matrix = [0,0,
            0,0]

    # gate 1
    dip_2.on()
    dip_3.on()
    if not dip_4.value():
        flags[0] = 0
    dip_2.off()
    if dip_4.value():
        flags[0] = 0
    dip_3.off()
    if dip_4.value():
        flags[0] = 0
    dip_2.on()
    if dip_4.value():
        flags[0] = 0

    # gate 2
    dip_5.on()
    dip_6.on()
    if not dip_7.value():
        flags[1] = 0
    dip_5.off()
    if dip_7.value():
        flags[1] = 0
    dip_6.off()
    if dip_7.value():
        flags[1] = 0
    dip_5.on()
    if dip_7.value():
        flags[1] = 0
        
    # gate 3
    dip_9.on()
    dip_10.on()
    if not dip_11.value():
        flags[2] = 0
    dip_9.off()
    if dip_11.value():
        flags[2] = 0
    dip_10.off()
    if dip_11.value():
        flags[2] = 0
    dip_9.on()
    if dip_11.value():
        flags[2] = 0
        
    # gate 4
    dip_12.on()
    dip_13.on()
    if not dip_14.value():
        flags[3] = 0
    dip_12.off()
    if dip_14.value():
        flags[3] = 0
    dip_13.off()
    if dip_14.value():
        flags[3] = 0
    dip_12.on()
    if dip_14.value():
        flags[3] = 0
        

    for i in range(4):
        if flags[i] == 1:
            matrix[i] = 1
        else:
            matrix[i] = 0
    
    return matrix