int pinA = 2;   // Le port D2 est associé à l'interruption 0
int pinB = 3;
volatile int pos = 0;  // Position (en nombre de pas) du codeur
 
void setup()  {
   Serial.begin(115200);
//   Serial.begin(9600);
   Serial.println("Codeur incremental");
   pinMode(pinA, INPUT);
   pinMode(pinB, INPUT);
   attachInterrupt(0, front, CHANGE);  // Détection des deux types de fronts
}
 
void loop()   {
//   delay(10);
}
 
void front()   {
   int sA = digitalRead(pinA);
   int sB = digitalRead(pinB);
   if (sA == sB)   {
      ++pos;
   }
   else   {
      --pos;
   }
   Serial.println(pos);     // Ligne à supprimer après les tests, car elle ralenti le dispositif
}
