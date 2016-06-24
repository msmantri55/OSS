/**
 * a program that prompts the user for the length of his or her shower in
 * minutes (as a positive integer, re-prompting as needed) and then prints the
 * equivalent number of bottles of water (as an integer), per the sample output
 * below, wherein underlined text represents some user’s input
 *
 * 1 minute shower = 12 bottles of water
 */

#include <cs50.h>
#include <stdio.h>

// get number of minutes for shower
int getMinutes(void) {
  printf("minutes: ");
  int minutes = GetInt();
  return minutes;
}

int main(void) {
  int minutes = getMinutes();

  // ensure that shower length is a positive value
  while (minutes <= 0) {
    printf("Retry: ");
    minutes = GetInt();
  }

  // return bottled water equivalent
  int bottles = minutes * 12;
  printf("bottles: %i\n", bottles);
}