current_IC=0  #for not gate change this to whatever ndex is used for other ICs
import machine
gpio=[4,5,6,7,9,10,11,12,24,25,26,27,32,34]
pinoutlist=[['OUT','IN','OUT','IN','OUT','IN','OUT','OUT','IN','OUT','IN','OUT','IN','OUT']]
truthtablelist=[[[1,0,1,0,1,0,0,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,0,1,0,1,0,1,0]]]
testcasecount=len(truthtablelist[current_IC])
testcaseerror=[]
for i in range(len(pinoutlist)):
    exec('dip_'+str(i)+'=machine.Pin('+str(gpio[i])+', Pin.'+pinoutlist[0][i]+')')
    if pinoutlist[0][i]=='OUT':
        exec('dip_'+str(i+'.value('+truthtablelist[0][testcasecount][i]+')'))
        
for i in range(len(pinoutlist)):
    if pinoutlist[0][i]=='OUT':
        continue
    exec('pinval=dip_'+str(i)+'value()')
    if truthtablelist[0][testcasecount][i] == pinval:
        continue
    else:
        testcaseerror.append(i)