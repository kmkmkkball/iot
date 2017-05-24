#include <wiringPi.h>
#include <stdio.h>

#define LedPin 5

int main(void) {


  if(wiringPiSetup() == -1){
    printf("setup wiringPi failed !");
      return 1;
  }
  printf("linker LedPin : GPIO %d(wiringPi pin)\n", LedPin);

  /* Pin:5 (WiringPi/GPIO:5 => BCM:24) */
  wiringPiSetup();
  pinMode(LedPin, OUTPUT);

  for(;;) {

    digitalWrite(LedPin, HIGH); delay(500);
    digitalWrite(LedPin, LOW); delay(500);

  }
}

