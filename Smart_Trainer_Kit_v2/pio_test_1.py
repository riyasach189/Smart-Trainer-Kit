import rp2
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)

def pio_prog():
    set(pins,1)
    
sm0 = rp2.StateMachine(0, pio_prog, set_base = Pin(25))
sm0.active(1)