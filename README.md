## Background and Motivation:
- The Digital Trainer Kit serves as a vital tool for facilitating learning, teaching, and testing of digital electronic circuits.
- It plays a crucial role in the laboratory component of the Digital Circuits course offered in Semester 1 at IIIT-D.
- However, the current trainer kits deployed in the ECE labs suffer from drawbacks such as being bulky, expensive, and featuring redundant functions.

## Objectives:
- To find alternatives that are compact, lightweight, and reasonably priced, without compromising essential functionalities.
- To enhance the versatility and functionality of the proposed alternative, a microcontroller will be incorporated into the design. This addition will provide opportunities for future expansion and the inclusion of advanced features, empowering students to explore more complex digital circuits.

## Version 1
**Components:**
- Arduino Board
- Red LEDs (x8) - For Input
- Blue LEDs (x8) - For Output
- Buck Boost Converter
- Resistors (330 Ohm)
- 6 Pin Mini Push Button Square Switch Self-Locking DPDT (x8)
- Green LEDs (x3) - For Clock Signals
- 4511 IC + 7 Segment Display (Common Cathode)
- Continuity Checker:
  - LED
  - Passive Buzzer
  - Resistor (330 Ohm)
- Voltage Detector:
  - 741 IC - As comparator
  - Resistors (330 Ohm) - For voltage divider
  - LED
- 5 mm Banana Sockets

**Features and Description:**
- A 12 V adapter powers the circuit. The Arduino has an inbuilt 12 V to 5 V converter. For the rest of the circuit, a Buck-Boost Converter is used.
- Nested 'for loops' are programmed in the Arduino to provide continuous clock signals of 3 frequencies - 0.1 Hz, 1 Hz, 10 Hz.
- The Continuity Checker can be used to debug faulty connections in a circuit.
- The Voltage Detector returns a HIGH value (LED turns on) when the voltage at a given point exceeds 2.5 V (to accommodate both the CMOS and TTL logic levels) in reference to the circuit ground, and returns a LOW value otherwise. A voltage divider is used between 5 V and GND to set the benchmark voltage at 2.5 V.
- The 4511 IC is connected to a 7-segment display to convert binary input to decimal digits (0 to 9).
- The Input LEDs can be operated using the Push Button switches connected to them.
- There are designated signal detector pins on the Arduino, which can be used to plot the clock signals on the Serial Plotter.

**Problems Encountered:**
- TinkerCad is not a reliable tool for large circuits; not recommended. They have also removed many components from their library.
- Initially, we planned to keep the clock frequencies variable, but Arduino can only run one infinite loop at a time. So, we decided to use nested 'for loops' to provide clock signals.
- We were trying to use a Common Cathode 7 segment display with a 7447 IC before we realized that that IC drives Common Anode displays.
- We found the 7805 IC unstable for voltage conversion, so we switched to a Buck-Boost Converter.
- When we kept the circuit on for a long time, the Input LEDs started flickering when switched ON. This issue remains unresolved. Possible reasons are:
  - The 12 V adapter could not meet the power requirements.
  - Arduino could not meet the power requirements.
  - The plastic and metal holes in the breadboard did not align, leading to loose connections.
  - Poor soldering on Buck-Boost Converter.
- We planned to use toggle switches in the circuit, but they were panel mount instead of PCB mount. So we switched to push button switches.

**Resources:**
- KiCad - PCB Design
- [7 Segment Display with 4511 IC](https://youtu.be/KZTwr95eINc)
- [Arduino for Beginners](https://youtu.be/d8_xXNcGYgo)
- [How to Use DPDT Switches](https://youtu.be/f0EMblUCp54)

## Version 2
**Components:**
- RPi Pico Board
- Red LEDs (x10) - For Input
- Blue LEDs (x10) - For Output
- Resistors (330 Ohm)
- Toggle switches (x10)
- 4511 IC + 7 Segment Display (Common Cathode)
- Continuity Checker:
  - Passive Buzzer
- 4 mm Banana Sockets
- Rotary Menu:
  - Rotary Encoder
  - LCD (16 x 2) + I2C
  - Potentiometer - For voltmeter
  - 16 Pin DIP Socket - For IC Tester
- Clock Generator - State machines on RPi Pico

**Features and Description:**
- A 5 V power supply powers the circuit.
- State machines on the rp2040 to provide continuous clock signals of 3 frequencies - 1 Hz, 5 Hz, 10 Hz.
- The Continuity Checker can be used to debug a circuit.
- The 4511 IC is connected to a 7-segment display to convert binary input to decimal digits (0 to 9).
- The Input LEDs can be operated using the toggle switches connected to them.
- The rotary menu is displayed on the LCD screen and operated using the rotary encoder. It has 2 options: IC Tester and Voltmeter.
- If 'Voltmeter' is selected, the LCD displays the voltage (in reference to the circuit GND) at the given point. To exit the voltmeter mode, click on the rotary encoder button.
- To use the IC Tester, plug the IC into the DIP socket (If it's a 14 Pin IC, leave the last 2 pins of the DIP Socket empty, i.e., start from the beginning of the DIP Socket). Then, select which IC you wish to test. The LCD will display '[ ]' for every gate that is functioning and '[!]' for every gate that is not functioning in the IC (keeping the IC notch on the left).

**Problems Encountered:**
- RPi Pico should connect to a Windows system in theory, but we were only able to establish connection in Linux systems.
- To connect an RPi Pico, we require a microUSB to USB cable which supports data and charge transfer, not just charge transfer.
- Pico's LED light did not turn ON the moment it was connected to the power supply, which led us to believe that the Pico was faulty (which is not true).
- It took us some time to decide between using a raw rotary encoder or one mounted on a PCB, due to differences in available online resources. We settled on a PCB-mounted encoder but re-soldered its header pins to be more breadboard-friendly.
- We decided to use an I2C to connect the LCD screen to reduce the number of pins required on RPi Pico. This left extra pins for IC Tester and future expansion.
- RPi Pico is a dual-core processor in theory, but we were unable to use its multithreading functionality. We spent a long time trying to generate clock signals from Pico on the second thread, but Pico could only process one thread at a time. We finally decided to use 555 timers to generate clock signals.
- For the voltmeter, we wanted a range of (0, 5) V but the analog read pins of RPi Pico can take a maximum input of 3.3 V. So we used a voltage divider to map the range (0, 5) V onto (0, 3.3) V, then mapped that back to (0, 5) V in the code.
- We were later able to implement a clock without the use of separate threads through state machines on three different pins; however, having a variable clock was still not possible, and we settled on having three constant clock signals.
- We replaced push button switches with toggle switches because they were shorting the GND and VCC plane in the ON configuration. We believe push button switches are available in 2 different pinouts, but they look the same on the outside, ie. it is not possible to tell from the outside which type of push button switch it is. Also, toggle switches offer more tactile feedback and are a better choice.
- The biggest bottleneck in the whole design process was finding a PCB manufacturer.
- We realised we had missed some traces in the PCB when we assembled the first prototype, so we added them later.
- We had missed the Vcc and GND connection of the 4511 IC, and for some reason, it was causing the IC to heat up whenever we turned the RPi Pico on. This problem was resolved when we provided Vcc and GND to the IC.

**Resources:**
- [Rotary Encoder with RPi Pico](https://youtu.be/sgnEUxeNxpM)
- [RPi Pico for Beginners](https://youtu.be/1WDagiA8fdU)
- [Connect LCD to RPi Pico using I2C](https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico)
- [555 Timer IC in Astable Mode](https://youtu.be/iJYm_BGqa1A)
- [555 Timer Frequency Calculator in Astable Mode](https://ohmslawcalculator.com/555-astable-calculator)
- [State Machines on the Rpi Pico](https://www.ourpcb.com/programmable-io.html)
  
## Contributors:
- [Riya Sachdeva - EVE, BTech 2026](https://github.com/riyasach189)
- [Surat Sathi Samanta - EVE, BTech 2026](https://github.com/kio42069/)
- [Aarav Mathur - CSSS, BTech 2026](https://github.com/13100d/)
