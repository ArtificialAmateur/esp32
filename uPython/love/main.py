from machine import I2C, Pin
from time import sleep
import ssd1306

# OLED Setup
rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
HEIGHT = 64
LENGTH = 128
oled = ssd1306.SSD1306_I2C(LENGTH, HEIGHT, i2c, addr=0x3c)

TEXT_SIZE = 8
HEART_SIZE = 9

# Display writing
HEART = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
]

while(True):
    oled.fill(0)

    oled.text('I', int((LENGTH/2) - ((len('I')*TEXT_SIZE) / 2)), 20)
    oled.text('love', int((LENGTH/2) - ((len('love')*TEXT_SIZE) / 2)), 30)
    oled.text('you', int((LENGTH/2) - ((len('you')*TEXT_SIZE) / 2)), 40)

    for y, row in enumerate(HEART):
        for x, c in enumerate(row):
            oled.pixel(x+int((LENGTH/2) - ((len('love')*TEXT_SIZE) / 2) - HEART_SIZE - 10), y+30, c)

    for y, row in enumerate(HEART):
        for x, c in enumerate(row):
            oled.pixel(x+int((LENGTH/2) + ((len('love')*TEXT_SIZE) / 2) + 10), y+30, c)
    oled.invert(0)
    oled.show()

    sleep(3)

    oled.fill(0)

    oled.text('I', int((LENGTH/2) - ((len('I')*TEXT_SIZE) / 2)), 20)
    oled.text('miss', int((LENGTH/2) - ((len('miss')*TEXT_SIZE) / 2)), 30)
    oled.text('you', int((LENGTH/2) - ((len('you')*TEXT_SIZE) / 2)), 40)

    for y, row in enumerate(HEART):
        for x, c in enumerate(row):
            oled.pixel(x+int((LENGTH/2) - ((len('miss')*TEXT_SIZE) / 2) - HEART_SIZE - 10), y+30, c)

    for y, row in enumerate(HEART):
        for x, c in enumerate(row):
            oled.pixel(x+int((LENGTH/2) + ((len('miss')*TEXT_SIZE) / 2) + 10), y+30, c)

    oled.invert(1)
    oled.show()
    sleep(3)
