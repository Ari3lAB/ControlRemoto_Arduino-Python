/*
   dht11.ino

   Este programa lee la humedad y temperatura usando el sensor
   DHT11

   Utiliza la biblioteca DHT.
*/

#include "DHT.h"
// Conecte la pata 1 del sensor (La de la izquierda) a +5V
// NOTA: Si se usa un arduino con logica de 3.3 volts como el
// Arduino Due conecte la pata 1 a 3.3V en lugar de 5V!
// Conecte la pata 2 del sensor a la pata del arduino dada por
// PIN_DHT
// Conecte la pata 4 del sensor (la de la derecha) a tierra
// Conecte una resistencia de 10K de la pata 2 (data) a la pata 1
// (5V) del sensor
const unsigned int PIN_DHT = 2;
const unsigned int BAUD_RATE = 9600;
// Inicialice el sensor DHT.
DHT dht(PIN_DHT, DHT11);
void setup() {
  Serial.begin(BAUD_RATE);
  Serial.println("Prueba del Sensor de humedad y temperatura DHT11!");

  dht.begin();
}
void loop() {
  // Espere unos segundos entre lecturas. La lectura de la
  // temperatura y humedadtoma unos 250 ms. Depende del sensor
  delay(2000);

  // Lee la humedad
  float h = dht.readHumidity();

  // Lee la temperatura en grados Celsius (por omision)
  float tc = dht.readTemperature();

  // Lee la temperatura en grados Fahrenheit
  //(isFahrenheit = true)
  float tf = dht.readTemperature(true);

  // Verifica si alguna lectura fallo y aborta
  // (para intentar de nuevo).
  if (isnan(h) || isnan(tc) || isnan(tf)) {
    Serial.println("Fallo la lectura del sensor DHT!");
    return;
  }

  // Calcula el indice de calor en grados Fahrenheit
  // (por omision)
  float hif = dht.computeHeatIndex(tf, h);
  // Calcula el indice de calor en grados Celsius
  // (isFahreheit = false)
  float hic = dht.computeHeatIndex(tc, h, false);

  Serial.print("Humedad: ");
  Serial.println(h);
  Serial.print("Temperatura: ");
  Serial.print(tc);
  Serial.print(" *C ");
  Serial.println(tf);
  Serial.print("Indice de calor: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F\n");
}
