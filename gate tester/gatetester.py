import machine

def gatetester(current_IC):
#for not gate change this to whatever index is used for other ICs

    current_IC = string_to_index(current_IC)

    gpio=[4,5,6,7,9,10,11,12,24,25,26,27,32,34]
    pinoutlist=[
        ['OUT','IN','OUT','IN','OUT','IN','OUT','OUT','IN','OUT','IN','OUT','IN','OUT'],  # 74LS04 not
        ['OUT','OUT','IN','OUT','OUT','IN','OUT','OUT','IN','OUT','OUT','IN','OUT','OUT'], # 74LS08 and
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4001 nor
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4011 nand
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4070 xor
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4071 or
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4077 xnor
        ['OUT','OUT','IN','IN','OUT','OUT','OUT','OUT','OUT','OUT','IN','IN','OUT','OUT'], # CD4081 and
        ['OUT','OUT','OUT','IN','OUT','OUT','IN','IN','OUT','OUT','IN','OUT','OUT','OUT'], # SN74LS157 mux
        ]
    truthtablelist=[
        [
            [1,0,1,0,1,0,0,0,0,1,0,1,0,1],                                                # 74LS04 not
            [0,1,0,1,0,1,0,0,1,0,1,0,1,0]
        ],
        [
            [1,1,1,1,1,1,0,0,1,1,1,1,1,1],                                                # 74LS08 and
            [1,0,0,1,0,0,0,0,0,0,1,0,0,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [1,1,0,0,1,1,0,0,1,1,0,0,1,1],                                                # CD4001 nor
            [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,0],
            [0,0,1,1,0,0,0,0,0,0,1,1,0,0]
        ],
        [
            [1,1,0,0,1,1,0,0,1,1,0,0,1,1],                                                # CD4011 nand
            [1,0,1,1,0,1,0,0,1,0,1,1,0,1],
            [0,1,1,1,1,0,0,0,0,1,1,1,1,0],
            [0,0,1,1,0,0,0,0,0,0,1,1,0,0]
        ],
        [
            [1,1,0,0,1,1,0,0,1,1,0,0,1,1],                                                # CD4070 xor
            [1,0,1,1,0,1,0,0,1,0,1,1,0,1],
            [0,1,1,1,1,0,0,0,0,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [1,1,1,1,1,1,0,0,1,1,1,1,1,1],                                                # CD4071 or
            [1,0,1,1,0,1,0,0,1,0,1,1,0,1],
            [0,1,1,1,1,0,0,0,0,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [1,1,1,1,1,1,0,0,1,1,1,1,1,1],                                                # CD4077 xnor
            [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,0],
            [0,0,1,1,0,0,0,0,0,0,1,1,0,0]
        ],
        [
            [1,1,1,1,1,1,0,0,1,1,1,1,1,1],                                                # CD4081 and
            [1,0,0,0,0,1,0,0,1,0,0,0,0,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ],
        [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1],                                                # SN74LS157 mux
            [0,0,1,0,0,1,0,0,1,0,0,1,0,1],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,1],
            [0,1,1,0,1,1,0,0,1,1,0,1,1,1],

            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,1,0,0,1,0,0,1,0,1],
            [1,1,0,0,1,0,0,0,0,1,0,0,1,1],
            [1,1,1,0,1,1,0,0,1,1,0,1,1,1],


            [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,0,1,1,1,1,0,1,1,0,0],
            [0,1,0,0,1,0,0,0,0,1,0,0,1,0],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,0],

            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,1,0,0,1,0,0,1,0,0,1,0,0],
            [1,1,0,1,1,0,1,1,0,1,1,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,0]
        ]
    ]

    testcasecountlimit = len(truthtablelist[current_IC])
    pinval = None
    testcaseerror = []

    for testcasecount in range(testcasecountlimit):
        for i in range(len(pinoutlist)):
            exec('dip_' + str(i) + '=machine.Pin(' + str(gpio[i]) + ', machine.Pin.' + pinoutlist[current_IC][i] + ')')
            if pinoutlist[current_IC][i] == 'OUT':
                exec('dip_' + str(i) + '.value(' + str(truthtablelist[current_IC][testcasecount][i]) + ')')
                
        for i in range(len(pinoutlist)):
            if pinoutlist[current_IC][i] == 'OUT':
                continue
            exec('pinval=dip_' + str(i) + '.value()')
            if truthtablelist[current_IC][testcasecount][i] == pinval:
                continue
            else:
                testcaseerror.append(gpio_to_gate(i, current_IC))

    return list(set(testcaseerror))


def gpio_to_gate(num, ic):
    if ic in [0,1,2,3,4,5,6,7]:
        if num < 6:
            return num + 1
        else:
            return num
    elif ic == 8:
        if num < 8:
            return num + 1
        else:
            return num + 2

def string_to_index(ic):
    ics = {"74LS04":0, "74LS08":1, "CD4001":2, "CD4011":3, "CD4070":4, "CD4071":5, "CD4077":6, "CD4081":7, "SN74LS157":8, "CD4013B":9, "74LS153":10}
    return ics[ic]

