#include <wiringPi.h>
#include <stdio.h>
#define LED_RED 4
#define LED_YELLOW 23
#define LED_GREEN 15

int main (void)
{
  wiringPiSetupGpio();
  pinMode (LED_RED, OUTPUT);
  pinMode (LED_YELLOW, OUTPUT);
  pinMode (LED_GREEN, OUTPUT);

  digitalWrite (LED_RED, HIGH) ; 
  delay (2000);
  printf("led red on\n");

  digitalWrite (LED_RED,  LOW) ; 
  delay (2000);
  printf("led red off\n");

  digitalWrite (LED_YELLOW, HIGH) ; 
  delay (2000);
  printf("led yellow on\n");

  digitalWrite (LE
  printf("led green off\n");

  pinMode (LED_RED, INPUT);
  pinMode (LED_YELLOW, INPUT);
  pinMode (LED_GREEN, INPUT);
  
  return 0;
}