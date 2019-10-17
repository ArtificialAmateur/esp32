from machine import I2C, Pin
import ssd1306
import time
import framebuf

# OLED Setup
rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
HEIGHT = 64
LENGTH = 128
oled = ssd1306.SSD1306_I2C(LENGTH, HEIGHT, i2c, addr=0x3c)


images = []
for n in range(1,10):
    with open('seanis.%s.pbm' % n, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    images.append(fbuf)

oled.invert(1)
while True:
    for i in images:
        oled.blit(i, 0, 0)
        oled.show()
        time.sleep(0.1)
