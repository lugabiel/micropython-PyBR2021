# main.py
# Using the ADC (Analogue to Digital Converter)
# Make sure you have the ADC checkbox marked!

import machine
import pyb
from time import sleep

# The slider is connected to pin Y4, try adjusting it
y4 = machine.Pin('Y4')
adc = pyb.ADC(y4)

while True:
    print(adc.read())
    sleep(0.5)