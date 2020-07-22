#include <Servo.h>

byte servoPin = 9;
byte potarPin = A0;
Servo servo;

int potar_min = 0;
int potar_max = 1023;
//int pwm_forward = 1560;
//int pwm_back = 1440;
int offset = 100;
int status_motor;
int pwm_signal;
int val_potar; // Set signal value, which should be between 1100 and 1900

void setup() {
  Serial.begin(9600);           //  setup serial
  pwm_signal = 1500 + offset;
  status_motor = true;
  
  servo.attach(servoPin);
  servo.writeMicroseconds(1500); // send "stop" signal to ESC.
  delay(2000); // delay to allow the ESC to recognize the stopped signal
}

void loop() {
  
  val_potar = analogRead(potarPin);  // read the input pin (0 to 1023)
  delay(val_potar);

  if (status_motor) {
    pwm_signal -= 2*offset;
  }
  else{
    pwm_signal += 2*offset;
  }
  status_motor = !status_motor;
  
  //Serial.println(val_potar);          // debug value
  Serial.println(pwm_signal);          // debug value
  
  servo.writeMicroseconds(pwm_signal); // Send signal to ESC.
}
