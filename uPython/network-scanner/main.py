from time import sleep
from machine import I2C, Pin
from network import WLAN, STA_IF
import ssd1306

# OLED Setup
rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.fill(0)

def wlan_scan():
    while(True):
        global oled
        wlan = WLAN(STA_IF)
        wlan.active(True)
        if wlan.isconnected():
            wlan.disconnect()
        list = wlan.scan()
        oled.fill(0)
        if not all(list):
            oled.text('Searching networks.', 0, 0)
            oled.show()
        else:
            oled.text('Networks found: ', 0, 0)
            oled.show()
        for i in range(len(list)):
            oled.text(list[i][0].decode(), 0, (i*8)+8)
            oled.show()
        sleep(5)

wlan_scan()
