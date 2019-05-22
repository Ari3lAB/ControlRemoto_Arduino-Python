#include "DHT.h" 
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
