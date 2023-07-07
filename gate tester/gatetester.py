
def gatetester(current_IC):
#for not gate change this to whatever ndex is used for other ICs
    exec("import machine")
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
            exec('dip_' + str(i) + '=machine.Pin(' + str(gpio[i]) + ', Pin.' + pinoutlist[current_IC][i] + ')')
            if pinoutlist[current_IC][i] == 'OUT':
                exec('dip_' + str(i + '.value(' + truthtablelist[current_IC][testcasecount][i] + ')'))
                
        for i in range(len(pinoutlist)):
            if pinoutlist[current_IC][i] == 'OUT':
                continue
            exec('pinval=dip_' + str(i) + '.value()')
            if truthtablelist[current_IC][testcasecount][i] == pinval:
                continue
            else:
                testcaseerror.append(gpio_to_gate(i, current_IC))

    return testcaseerror


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
    match ic:
        case "74LS04":
            return 0
        case "74LS08":
            return 1
        case "CD4001":
            return 2
        case "CD4011":
            return 3
        case "CD4070":
            return 4
        case "CD4071":
            return 5
        case "CD4077":
            return 6
        case "CD4081":
            return 7
        case "SN74LS157":
            return 8
        case "CD4013B":
            return 9
        case "74LS153":
            return 10
        
gatetester(0)