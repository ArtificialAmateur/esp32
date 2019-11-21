#include <U8g2lib.h>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C       u8g2(U8G2_R0, 16, 15, 4);         // OLED graphics

void setup() {
  // put your setup code here, to run once:
  u8g2.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_6x10_tr);
    u8g2.drawStr(0,15,"Hello World");
  } while(u8g2.nextPage());
  delay(1000);
}
