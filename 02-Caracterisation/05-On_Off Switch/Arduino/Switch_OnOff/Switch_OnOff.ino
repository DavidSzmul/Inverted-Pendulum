byte switchPin = 22;

void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {

  int val = digitalRead(switchPin);   // read the input pin
  delay(10);
  Serial.println(val);          // debug value
  }
