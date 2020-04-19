
// Import required libraries
#include "ArducamSSD1306.h"    // Modification of Adafruit_SSD1306 for ESP8266 compatibility
#include "Adafruit_GFX.h"   // Needs a little change in original Adafruit library (See README.txt file)
#include <Wire.h>           // For I2C comm, but needed for not getting compile error

/*
HardWare I2C pins
A4   SDA
A5   SCL
*/

// Pin definitions
#define OLED_RESET  16  // Pin 15 -RESET digital signal

#define LOGO16_GLCD_HEIGHT 16
#define LOGO16_GLCD_WIDTH  16

ArducamSSD1306 display(OLED_RESET); // FOR I2C


void setup(void)
{
	// Start Serial
	Serial.begin(115200);

  // SSD1306 Init
  display.begin();  // Switch OLED
  // Clear the buffer.
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(20,20);
  display.println("Smart Fishtank");
  display.setCursor(20,40);
  display.println("initializing...");
  display.display();
//initialize rest of sensors here

//
}



void loop() {
  //concatenate remaining sensor values onto ends of strings
delay(2000);
display.clearDisplay();
display.setCursor(0,0);
display.setTextSize(2);
display.println("Smart Tank");
display.setCursor(0,20);
display.setTextSize(1);
display.println("Temp:F");
display.setCursor(0,35);
display.println("Clarity:xxxx");
display.setCursor(0,50);
display.println("PH:xxxx");
display.display();
delay(10000);
display.clearDisplay();
display.setCursor(20,20);
display.setTextSize(3);
display.println("reset");
display.display();

}
