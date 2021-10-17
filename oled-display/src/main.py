# main.py

# A fully simulated I2C bus and LCD Display
# The framebuf class simplifies graphics in MicroPython
# Use the hardware i2c in example Pong for faster performance
# Make sure you have the I2C LCD checkbox marked!

import machine
import framebuf

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)

fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

logo = framebuf.FrameBuffer(bytearray(17 * 17 // 8), 17, 17, framebuf.MONO_HLSB)

logo.fill(0)
logo.fill_rect(1, 1, 15, 15, 1)
logo.vline(4, 4, 12, 0)
logo.vline(8, 1, 12, 0)
logo.vline(12, 4, 12, 0)
logo.vline(14, 13, 2, 0)
print(logo.)

fbuf.fill(0)
fbuf.blit(logo, 23, 7)

i2c.writeto(8, fbuf)
