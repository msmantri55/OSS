/**
 * program that first asks the user how much change is owed and then spits out
 * the minimum number of coins with which said change can be made. Use GetFloat
 * from the CS50 Library to get the user’s input and printf from the Standard
 * I/O library to output your answer. Assume that the only coins available are
 * quarters, dimes, nickels, and pennies.
 */

#include <cs50.h>
#include <stdio.h>
#include <math.h>

// get amount of change owed
int main(void) {
  printf("How much change is owed?\n");

  // multiply by 100 to get cents, convert float to int by rounding
  int cents = (int) round(GetFloat() * 100);

  // ensure that amount owed is a positive value
  while (cents <= 0) {
    printf("Retry: ");
    cents = (int) round(GetFloat() * 100);
  }

  int coins = 0;
  int coinValues[4] = {25, 10, 5, 1};

  // for each coin increment amount of coins and decrement remaining amount owed
  for (int i = 0; i < sizeof(coinValues) / sizeof(coinValues[0]); i++) {
    coins += cents / coinValues[i];
    cents = cents % coinValues[i];
  }

  printf("%i\n", coins);
}