# Example using PIO to blink an LED and raise an IRQ at 1Hz.

import utime
from machine import Pin
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)

def blink_1hz():
    # Cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    irq(rel(0))
    set(pins, 1)
    set(x, 31)                  [5]
    label("delay_high")
    nop()                       [29]
    jmp(x_dec, "delay_high")

    # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)
    set(x, 31)                  [6]
    label("delay_low")
    nop()                       [29]
    jmp(x_dec, "delay_low")

# Create the StateMachine with the blink_1hz program, outputting on Pin(25).
sm_1 = rp2.StateMachine(0, blink_1hz, freq=2000, set_base=Pin(9))   # 9 is 1 hz
sm_5 = rp2.StateMachine(1, blink_1hz, freq=10000, set_base=Pin(10))   # 10 is 0.1 hz
sm_10 = rp2.StateMachine(2, blink_1hz, freq=20000, set_base=Pin(11))   # 11 is 10 hz

# Set the IRQ handler to print the millisecond timestamp.
sm_1.irq(lambda p: print(end = ''))  #print(utime.ticks_ms())
sm_5.irq(lambda p: print(end = ''))
sm_10.irq(lambda p: print(end = ''))

# Start the StateMachine.
#sm_1.active(1)