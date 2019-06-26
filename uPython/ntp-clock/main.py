from machine import I2C, Pin, RTC
from network import WLAN, STA_IF
from usocket import getaddrinfo, socket
import ssd1306
import time

# OLED Setup
rst = Pin(16, Pin.OUT)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.fill(0)

NTP_PACKET_LENGTH = 48
NTP_DELAY_COUNT = 20
TIME_ZONE = -5
UDP_PORT = 4000

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

def get_time():
    global NTP_DELAY_COUNT
    global NTP_PACKET_LENGTH
    ntpDelay = NTP_DELAY_COUNT
    while(True):
        if timeReceived == False:
            ntpDelay += 1
            if ntpDelay >= NTP_DELAY_COUNT:
                # Reset delay
                ntpDelay = 0
                ntpPacket = b'0b00011011'

                # Send ntp packet
                s = socket()
                s.connect(getaddrinfo('129.6.15.28', 123)[0][-1])
                s.write(ntpPacket)

                print("NTP clock: ntp packet sent to ntp server.")
                print("NTP clock: awaiting response from ntp server")

            # Check for time to check for server response
            if ntpDelay == (NTP_DELAY_COUNT - 1):
                # Read server response
                response = s.read(NTP_PACKET_LENGTH)

                # obtain time from packet, convert, and adjust for tz
                timevalue = [(response[40] << 24), (response[41] << 16), (response[42] << 8), response[43], (((70 * 365) + 17) * 86400), (TIME_ZONE + 3600), 5]

                rtc = RTC()
                rtc.init(())

                # time has been received
                timeReceived = True
