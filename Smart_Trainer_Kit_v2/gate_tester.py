import machine
import time
from constants import *
def gatetester(current_IC):
#for not gate change this to whatever index is used for other ICs
    current_IC = ics[current_IC]
    testcasecountlimit = len(truthtablelist[current_IC])
    testcaseerror = []
    for testcasecount in range(testcasecountlimit):
        for i in range(len(pinoutlist[current_IC])):
            exec('dip_'+str(i)+'=machine.Pin(' + str(gpio[i]) + ', machine.Pin.' + pinoutlist[current_IC][i] + ')')
            
            if pinoutlist[current_IC][i] == 'OUT':
                eval('dip_'+str(i) + '.value(' + str(truthtablelist[current_IC][testcasecount][i]) + ')')
                
        time.sleep(0.05)
        
        for i in range(len(pinoutlist[current_IC])):
            #print(i)
            #print(testcasecount, "HUHU")
            if pinoutlist[current_IC][i] == 'OUT':
                continue
            
            pinval = eval('dip_' + str(i) + '.value()')
            if truthtablelist[current_IC][testcasecount][i] == pinval:
                continue
            
            else:
                print("REAL: ", pinval, "EXPECTED: ", truthtablelist[current_IC][testcasecount][i], "PIN: ", i, "TEST CASE: ", testcasecount)
                testcaseerror.append(eval('cat'+str(icindextocategory[current_IC])+'('+str(i)+')'))

                
    print(testcaseerror)
    
    return list(set(testcaseerror))

