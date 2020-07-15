// I2C Scanner

#include <WSWire.h>

void setup() {
Serial.begin (9600);
Serial.println ();
Serial.println ("I2C scanner. Scanning ...");
byte count = 0;

Wire.begin();
for (byte i = 8; i < 120; i++){
  Wire.beginTransmission(i);
  delay(1);
  Serial.print(i);
  byte error = Wire.endTransmission();
  delay(1);
  Serial.print(i);
  if (error == 0){
    Serial.print ("Found address: ");
    Serial.print (i, DEC);
    Serial.print (" (0x");
    Serial.print (i, HEX);
    Serial.println (")");
    count++;
    delay (1);
  } // end of good response
} // end of for loop
Serial.println ("Done.");
Serial.print ("Found ");
Serial.print (count, DEC);
Serial.println (" device(s).");
}

void loop() {}
