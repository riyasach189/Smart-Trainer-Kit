#sm.exec also works
import time
import rp2
from machine import Pin

@rp2.asm_pio(set_init = rp2.PIO.OUT_LOW)

# def bounce():
#     pull()   #pull from tx fifo and put in output shift register
#     mov(isr, osr) #moves content of osr to isr
#     push()   #pushes content of isr onto rx fifo
    
def doubleit():
    pull()
    in_(osr, 32) #move value of osr into isr by 32 bits
    set(x,0)
    in_(x,1)     #left shift by 1
    push()
    
#sm = rp2.StateMachine(0, bounce, freq=2000, set_base = Pin(25))
sm = rp2.StateMachine(0, doubleit, set_base = Pin(25))

sm.put(31)  #put 31 on tx queue

print("Number of words in tx", sm.tx_fifo())  #input queue
print("Number of words in rx", sm.rx_fifo())  #output queue
print("Run")

sm.active(1)
time.sleep(1)
print("Stop")
sm.active(0)
print("Number of words in tx", sm.tx_fifo())
print("Number of words in rx", sm.rx_fifo())
print("Get from rx", sm.get())