#include <LiquidCrystal.h>
#include <dht.h>

LiquidCrystal lcd(12,11,5,4,3,2);

dht DHT;

#define DHT11_PIN 8

void setup(){
  lcd.begin(16,2);
}

void loop(){
  int chk = DHT.read11(DHT11_PIN);
  lcd.setCursor(0,0);
  lcd.print("Temp: ");
  lcd.setCursor(8,0);
  lcd.print(DHT.temperature);
  lcd.print("C");
  lcd.print((char)223);
  lcd.setCursor(0,1);
  lcd.print("Fukt: ");
  lcd.setCursor(8,1);
  lcd.print(DHT.humidity);
  lcd.print("%");
  delay(2000);
}
