int pausa = 1000;

void setup() {
  Serial.begin(9600);
  while (!Serial.available()) {
  }
}

void loop() {
  if (Serial.available()) {
    char var = Serial.read();
    switch (var) {
      case '0':
        Serial.println("10");
        break;
      case '1':
        Serial.println("37");
        break;
    }
    Serial.flush();
    delay(pausa);
  }
}
