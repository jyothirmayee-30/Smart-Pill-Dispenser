#include <WiFiNINA.h>
#include <RTCZero.h>
#include <Servo.h>

RTCZero rtc;
Servo trayServo;
const int irPin = 7;

void setup() {
  Serial.begin(9600);
  rtc.begin();
  trayServo.attach(9);
  pinMode(irPin, INPUT);
  // WiFi and NTP Time Sync logic here
}

void loop() {
  // Logic to check if current time matches Dose_Time
  if (rtc.getHours() == 8 && rtc.getMinutes() == 0) {
    dispense();
  }
}

void dispense() {
  trayServo.write(90); // Move to next compartment
  delay(1000);
  trayServo.write(0);
  
  // Wait to see if IR sensor detects pill removal
  bool taken = digitalRead(irPin);
  Serial.println(taken ? "Taken" : "Missed");
}
