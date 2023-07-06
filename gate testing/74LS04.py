# not
# vcc io io io
# io io io gnd

def not_74LS04():
    import machine

    dip_2 = machine.Pin(4, Pin.OUT)
    dip_3 = machine.Pin(5, Pin.IN)

    dip_4 = machine.Pin(6, Pin.OUT)
    dip_5 = machine.Pin(7, Pin.IN)

    dip_6 = machine.Pin(9, Pin.OUT)
    dip_7 = machine.Pin(10, Pin.IN)

    dip_9 = machine.Pin(11, Pin.OUT)
    dip_10 = machine.Pin(12, Pin.IN)

    dip_11 = machine.Pin(24, Pin.OUT)
    dip_12 = machine.Pin(25, Pin.IN)

    dip_13 = machine.Pin(26, Pin.OUT)
    dip_14 = machine.Pin(27, Pin.IN)

    flags = [1,1,1,
            1,1,1]

    matrix = [0,0,0
            ,0,0,0]

    dip_2.on()
    dip_4.on()
    dip_6.on()
    dip_9.on()
    dip_11.on()
    dip_13.on()


    if dip_3.value():
        flags[0] = 0
    if dip_5.value():
        flags[1] = 0
    if dip_7.value():
        flags[2] = 0
    if dip_10.value():
        flags[3] = 0
    if dip_12.value():
        flags[4] = 0
    if dip_14.value():
        flags[5] = 0

    dip_2.off()
    dip_4.off()
    dip_6.off()
    dip_9.off()
    dip_11.off()
    dip_13.off()


    if not dip_3.value():
        flags[0] = 0
    if not dip_5.value():
        flags[1] = 0
    if not dip_7.value():
        flags[2] = 0
    if not dip_10.value():
        flags[3] = 0
    if not dip_12.value():
        flags[4] = 0
    if not dip_14.value():
        flags[5] = 0

    for i in range(6):
        if flags[i] == 1:
            matrix[i] = 1
        else:
            matrix[i] = 0
