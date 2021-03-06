#include <Arduino.h>
// Import required libraries
#include "ArducamSSD1306.h" // Modification of Adafruit_SSD1306 for ESP8266 compatibility
#include "Adafruit_GFX.h"   // Needs a little change in original Adafruit library (See README.txt file)
#include <Wire.h>           // For I2C comm, but needed for not getting compile error

#include <OneWire.h>
#include <DallasTemperature.h>

#include <WString.h>

#define MAX_BUFFER_SIZE 256
#define D_PRINT Serial.println(F("DEBUG"));

/*
HardWare I2C pins
A4   SDA
A5   SCL
*/

// Pin definitions
#define OLED_RESET 16 // Pin 15 -RESET digital signal

#define LOGO16_GLCD_HEIGHT 16
#define LOGO16_GLCD_WIDTH 16

#define STRING_IN(str) else if (!strcmp(input, str))

const char COMMAND_PH[] = "ph";
const char COMMAND_POTENTIOMETER[] = "potentiometer";
const char COMMAND_TEMPERATURE[] = "temperature-sensor";
const char DEBUG_CSTR_PARSER[] = "debug-cstring-parser";

// Analog Inputs
const int PH_SENSOR = 0;
const int POTENTIOMETER_0 = 1;
const int POTENTIOMETER_1 = 2;
const char END_LINE_MAP[] = {0, '\n', 13, ' '};

// Digital Inputs
const int ONE_WIRE_BUS = 2; // Temperature sensors

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensors(&oneWire);
ArducamSSD1306 display(OLED_RESET); // FOR I2C

void printStringHex(const char *cstr, bool newline = false);
char *storeSerial(char *cstr, bool wait, int size = 0, bool overflowProtect = false, int growth = 16);
int cstringToInt(char *cstr);

void setup(void)
{
    // Start Serial
    Serial.begin(9600);
	Serial.println(F("Initializing"));

    // SSD1306 Init
    display.begin(); // Switch OLED
    // Clear the buffer.
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(20, 20);
    display.println(F("Smart Fishtank"));
    display.setCursor(20, 40);
    display.println(F("initializing..."));
    display.display();
    //initialize rest of sensors here

    // Setting up sensors
	tempSensors.begin();
	Serial.println(F("Done finishing up sensors"));
	delay(1000);
	// for (int i = 0; i < 100; ++i) Serial.print('\0');
    //
}

void loop()
{
	// delay(1000);
	char input[MAX_BUFFER_SIZE];
	input[0] = '\0';
	storeSerial(input, false);
	

	// Serial.println(F"Available!");

	if (!strcmp(input, "potentiometer"))
	{

		// Serial.print(F"Potentiometer: ");
		Serial.println(analogRead(POTENTIOMETER_0) / 1024.0 * 5.0);
	}
	else if (!strcmp(input, "ph"))
	{
		// Serial.print(F"PH: ");
		Serial.println(analogRead(PH_SENSOR) / 1024.0 * 5.0 * 3.5);
	}
	else if (!strcmp(input, "temperature-sensor"))
	{
		char numInput[32];
		storeSerial(numInput, true);

		if (!strcmp(numInput, "count")) {

			// Serial.print(F"Count: ");
			Serial.println(tempSensors.getDeviceCount(), DEC);
		}
		else {
			
			int id = cstringToInt(numInput);
			int numDevices = tempSensors.getDeviceCount();

			if (id < 0) Serial.println(F("invalid-id"));
			else if (id >= numDevices) Serial.println(F("out-of-bounds-id"));
			else Serial.println(tempSensors.getTempCByIndex(id));
		}
	}
	else if (!strcmp(input, "signal-error")) {

		
	}
	
	else if (!strcmp(input, "man") || !strcmp(input, "help"))
	{
		Serial.println(F("potentiometer ph temperature-sensor"));
	}
    //concatenate remaining sensor values onto ends of strings
    // delay(2000);
    display.clearDisplay();
    display.setCursor(0, 0);
    display.setTextSize(1);
    display.println(F("Smart Tank"));
    //calc avg temp
    display.setCursor(0, 12);
    display.setTextSize(1);
    int temp = (tempSensors.getTempCByIndex(0) + tempSensors.getTempCByIndex(1))/2; 
    //print temp
    display.print(F("Temp: "));
    display.print(temp);
    display.println(F("C"));
    //print clarity	
    display.setCursor(0, 24);
    display.print(F("Clarity:"));
    display.print(rand()%5);
    display.println();
    //print ph
    display.setCursor(0, 36);
    display.print(F("PH:"));
    display.print((analogRead(PH_SENSOR)/1024.0*5.0*3.5));
    display.println();
    //print set temp
    display.setCursor(0,48);
    display.print(F("Set Temp:"));
    display.print((analogRead(POTENTIOMETER_0)/50)+60);
    display.println();
    display.display();

	/* If statements over here for audio */

	Serial.flush();

}

/**
 * TODO add comment
 */
char * storeSerial(char *cstr, bool wait, int size, bool overflowProtect, int growth)
{
	if (wait) {
		while (!Serial.available()) { }

	}
		
	int allocateSize = size;
	if (Serial.available()) {
		int cnt = 0;
		cstr[0] = Serial.read();

		while (!isCharacter(cstr[cnt], END_LINE_MAP, sizeof(END_LINE_MAP))) {

			while (!Serial.available()) {}
			++cnt;

			// if overflow protection is enabled and cstr overflows, a new buffer
			// is created and will be returned
			if (overflowProtect && cnt >= allocateSize) {

				allocateSize += growth;
				char *buff = new char[allocateSize];
				strcpy(buff, cstr);
				cstr = buff;
			}
			
			cstr[cnt] = Serial.read();
			// Serial.print(cstr[cnt]);
		}

		cstr[cnt] = 0;
		// Serial.println(F"\nDone!");
		// Serial.println(cstr);
		// printStringHex(cstr, true);

	}
	else {
		cstr[0] = '\0';
		// Serial.println(F"HERE!");

		// delay(500);
	}

	return allocateSize == size ? nullptr : cstr;
}

bool isCharacter(char c, const char *charMap, int size)
{
	for (int i = 0; i < size; ++i)
	{

		if (c == charMap[i])
			return true;
	}

	return false;
}

/**
 * Converts a cstring that contains a number to an 
 * integer ("1" -> 1, "24" -> 24, "3234" -> 3234)
 * char *cstr - cstring containing a number
 * return - integer from cstring
 * 
 * WARNING - This does not check if the characters in
 * the cstring is a valid digit
 */
int cstringToInt(char *cstr)
{
	int val = 0;
	char *c = cstr;
	
	while (*c != '\0') {

		if (*c == '-') {

			val *= -1;
		}
		else {

			val *= 10;
			val += *c - 0x30;
			++c;
		}
	}

	return val;
}

void printStringHex(char* cstr, bool newline)
{
	if (cstr[0] != '\0') Serial.print(cstr[0], HEX);
	
	for (char *c = cstr + 1; *c != '\0'; ++c) {

		Serial.print(F(" "));
		Serial.print(*c, HEX);
	}

	if (newline) Serial.println();
}
// 
