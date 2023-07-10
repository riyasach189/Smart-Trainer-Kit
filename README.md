# Background and Motivation:
- The Digital Trainer Kit serves as a vital tool for facilitating learning, teaching, and testing of digital electronic circuits.
- It plays a crucial role in the laboratory component of the Digital Circuits course offered in Semester 1 at IIIT-D.
- However, the current trainer kits deployed in the ECE labs suffer from drawbacks such as being bulky, expensive, and featuring redundant functions.

# Objectives:
- To find alternatives that are compact, lightweight, and reasonably priced, without compromising essential functionalities.
- To enhance the versatility and functionality of the proposed alternative, a microcontroller will be incorporated into the design. This addition will provide opportunities for future expansion and the inclusion of advanced features, empowering students to explore more complex digital circuits.

# Version 1
## Components:
- Arduino Board
- Jumper wires
- Breadboards (x3)
- Red LEDs (x8) - For Input
- Blue LEDs (x8) - For Output
- Buck Boost Converter
- Resistors (330 Ohm)
- 6 Pin Mini Push Button Square Switch Self-Locking DPDT (x8)
- Green LEDs (x3) - For Clock Signals
- 4511 IC + 7 Segment Display (Common Cathode)
- Continuity Checker:
  - Breadboard Mini
  - LED
  - Passive Buzzer
  - Resistor (330 Ohm)
  - 9V Battery
- Voltage Detector:
  - 741 IC - As comparator
  - Resistors (330 Ohm) - For voltage divider
  - LED
- 5 mm Banana Sockets

## Features and Description:
- The circuit is powered by a 12 V adapter. The Arduino has an inbuilt 12 V to 5 V converter. For the rest of the circuit, a Buck Boost Converter is used.
- Nested 'for loops' are programmed in the Arduino to provide continuous clock signals of 3 frequencies - 0.1 Hz, 1 Hz, 10 Hz.
- The Continuity Checker can be used to debug a circuit.
- The Voltage Detector returns a HIGH value (LED turns on) when the voltage at a given point is more than 2.5 V in reference to the circuit ground, and returns a LOW value otherwise. A voltage divider is used between 5 V and GND to set the benchmark voltage at 2.5 V.
- The 4511 IC is connected to a 7 segment display to convert binary input to decimal digits (0 to 9).
- The Input LEDs can be operated using the Push Button switches connected to them.
- There are designated signal detector pins on the Arduino, which can be used to plot the clock signals on the Serial Plotter.

## Problems Encountered:
- Initial TinkerCad Design: Circuit design Ingenious Rottis-Bruticus | Tinkercad
- TinkerCad is not a very reliable tool for large circuits; not recommended. They have also removed many components from their library.
- Plastic and metal holes didn't align in the breadboards, which often led to loose connections.
- We used breadboards of different manufacturers, so we were unable to connect them together. Also, power rails were disconnected in the middle in some breadboards and were connected in others.
- Initially, we were planning to keep the clock frequencies variable, but Arduino can only run 1 infinite loop at a time. So, we decided to use nested 'for loops' to provide clock signals.
- We were trying to use a Common Cathode 7 segment display with a 7447 IC, before we realized that that IC drives Common Anode displays.
- We found the 7805 IC to be unstable for voltage conversion, so we switched to a Buck Boost Converter.

## Resources:
- KiCad - PCB Design
- 7 Segment Display with 4511 IC
- Arduino for Beginners
- How to Use DPDT Switches

# Version 2
## Components:

## Features and Description:

## Problems Encountered:

## Resources:
- Rotary Encoder with RPi Pico
- RPi Pico for Beginners
- Connect LCD to RPi Pico using I2C
- 555 Timer IC in Astable Mode
- 555 Timer Frequency Calculator in Astable Mode

# Contributors:
- Dr. Rahul Gupta - Manager, Research Labs (Supervisor of the Project)
- Riya Sachdeva - EVE, BTech 2026
- Surat Sathi Samanta - EVE, BTech 2026
- Aarav Mathur - CSSS, Btech 2026

# Collaborators
[@riyasach189](https://www.github.com/riyasach189)

[@surat-ss](https://www.github.com/surat-ss)

[@13100D](https://github.com/13100D)
