/*
This code is run on the Arduino and will show errors not found on the Arduino.
*/

// GLOBAL VARIABLES

const int numLEDs = 10;
bool calc = false;
int ledPins[numLEDs] = {4, 5, 6, 7, 8, 9, 10, 11, 12}; // Change these pin numbers according to your setup
bool lightOn[numLEDs] = {true, true, true, true, true, true, true, true, true, true};
int receivedInt;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  // Baud rate
  }

void loop() {
  while (Serial.available() > 0) {
    receivedInt = Serial.read();
    Serial.println(receivedInt);
    calc = true;
  }
  
  while (calc) {

    // This is where we calculate the list
    for (int i = 10 - 1; i >= 0; i--) {
      lightOn[i] = receivedInt & 0x01;
      receivedInt >>= 1;
    }

    for (int i = 0; i < numLEDs; i++) {
      if (!lightOn[i]) {
        digitalWrite(ledPins[i], HIGH); // Turn the LED on
      } else {
        digitalWrite(ledPins[i], LOW); // Turn the LED off
      }
    }
    calc = false;
  }
}
