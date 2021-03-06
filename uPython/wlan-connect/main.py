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

def wlan_connect():
    global oled
    wlan = WLAN(STA_IF)                      # create station interface
    wlan.active(True)                        # bring interface up
    if not wlan.isconnected():
        oled.text('Connecting to network...', 0, 0)
        wlan.connect('SSID', 'PASS')
        oled.text(wlan.config('essid'), 20, 35)
        oled.show()
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())

wlan_connect()
