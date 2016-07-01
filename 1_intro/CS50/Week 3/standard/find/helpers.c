/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int array[], int n)
{
  bool flag = false;
  for (int i = 0; i < n; i++) {
    if (value == array[i]) {
      flag = true;
    }
  }
  return flag;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
  int sorted[n];
  for (int outer = 0; outer < n; outer++) {
    int max = 0;
    int index = 0;
    for (int i = 0; i < n; i++) {
      if (values[i] > max) {
        max = values[i];
        index = i;
      }
    }
    sorted[outer] = max;
    values[index] = 0;
  }

  for (int i = 0; i < n; i++) {
    values[i] = sorted[i];
  }

  return;
}