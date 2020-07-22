#include <Servo.h>

byte servoPin = 9;
byte potarPin = A0;
Servo servo;

int potar_min = 0;
int potar_max = 1023;
int pwm_max = 1900;
int pwm_min = 1100;

int val_potar; // Set signal value, which should be between 1100 and 1900
int pwm_signal; // Set signal value, which should be between 1100 and 1900
int bias_pwm;   // Scale is supposed to be 1

void setup() {
  Serial.begin(9600);           //  setup serial
  bias_pwm = ((pwm_max+pwm_min)- (potar_max + potar_min))/2;

  servo.attach(servoPin);
  servo.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(7000); // delay to allow the ESC to recognize the stopped signal
}

void loop() {

  val_potar = analogRead(potarPin);  // read the input pin (0 to 1023)
  pwm_signal = max(min(val_potar+bias_pwm, pwm_max),pwm_min);
  
  //Serial.println(val_potar);          // debug value
  Serial.println(pwm_signal);          // debug value
  
  servo.writeMicroseconds(pwm_signal); // Send signal to ESC.
}
