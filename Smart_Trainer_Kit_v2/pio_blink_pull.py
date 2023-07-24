import time
from machine import Pin
import rp2

@rp2.asm_pio(out_init = rp2.PIO.OUT_LOW)

def blink_pull():
    wrap_target()
    pull()
    set(x, 31)
    label("bitloop")
    out(pins, 1)       [31]
    jmp(x_dec, "bitloop")   #decrement x by 1, jump if it's not 0
    wrap()
    
sm = rp2.StateMachine(1, blink_pull, freq = 2000, out_shiftdir = rp2.PIO.SHIFT_RIGHT, out_base = Pin(25))

sm.active(1)

while True:
    sm.put(0x00000001) 