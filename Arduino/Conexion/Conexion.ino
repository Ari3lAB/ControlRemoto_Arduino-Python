#include "DHT.h"
#include <SoftwareSerial.h>
#include <string.h>



SoftwareSerial Sim900Serial(7, 8);      //SIM900 Tx & Rx is connected to Arduino #7 & #8


const unsigned int PIN_DHT = 2;
const unsigned int BAUD_RATE = 9600;
const unsigned int PIN_LED = 4;
int pausa = 1000;


#define phonenumber "526444609146"     //Numero de teléfono que enviará los mensajes

DHT dht(PIN_DHT, DHT11);
byte buffer[64]; //Buffer para recivir datos del puerto serie
int count = 0;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, LOW);

  Serial.begin(BAUD_RATE);
  Sim900Serial.begin(BAUD_RATE);    //Velocidad del puerto serie por Software pines 7 y 8


  dht.begin();                      //Sensor de temp y humedad

  while (!Serial.available()) {
  }
}


void loop() {
  char var;
  float h = dht.readHumidity(); // Lee la humedad
  float tc = dht.readTemperature(); // Lee la temperatura en grados Celsius (por omision)
  
  
    
  
  if (Serial.available()) {
    
    //Switch para seleccionar la accion a realizar
    var = Serial.read();

    switch (var) {
      case '0':
        Serial.println(tc);//imprime la temp. en celcius
        break;

      case '1':
        Serial.println(h);//Imprime el nivel de humedad
        break;

      case '2': //Cambia de estado el abanico
        if (digitalRead(PIN_LED) == HIGH) {
          digitalWrite(PIN_LED, LOW);
          Serial.println("OFF");
        } else {
          digitalWrite(PIN_LED, HIGH);
          Serial.println("ON");
        }
        break;

      case '3'://Regresa el estado del abanico
        if (digitalRead(PIN_LED) == HIGH) {
          Serial.println("ON");
        } else {
          Serial.println("OFF");
        }
        break;
    }
  }
  delay(pausa);
}

void checkSerial(){
  if (Sim900Serial.available())
    {
      while (Sim900Serial.available())         //Leyendo datos del arreglo de caracteres
      {
        buffer[count++] = Sim900Serial.read();   //Almacenando los datos del arreglo en un buffer
        if (count == 64)break;
      }
      Serial.write(buffer, count);
      Cmd_Read_Act();
      clearBufferArray();
      count = 0;
    }

    if (Serial.available())            // Verifica si se dispone de datos en el puerto serie por hardware
      Sim900Serial.write(Serial.read());       // y los escribe en el escudo SIM900
}

void clearBufferArray()
{
  for (int i = 0; i < count; i++)
  {
    buffer[i] = NULL; // borrar todos los índices del arreglo
  }
}
void Sim900_Inti(void)
{
  Sim900Serial.println("AT+CMGF=1");
  delay(500);
  Sim900Serial.println("AT+CNMI=2,2");
  delay(500);
}

//////Esta función lee los SMS enviados al escudo SIM900 y actua en base a esa orden.
void Cmd_Read_Act(void)
{
  char buffer2[64];
  char comparetext[25];
  for (int i = 0; i < count; i++)
  {
    buffer2[i] = char(buffer[i]);
  }
  memcpy(comparetext, buffer2, 25);

    ///////////LED4///////////////////////////////////////
    if (strstr(buffer2, "On4"))
    {
      digitalWrite(PIN_LED, HIGH);
    }
    if (strstr(buffer2, "Off4"))
    {
      digitalWrite(PIN_LED, LOW);
    }  
}
