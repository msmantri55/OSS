/**
 * program that recreates Mario half-pyramids using hashes (#) for blocks.
 * First prompt the user for the half-pyramids' heights, a non-negative integer
 * no greater than 23.
 * Then, generate (with the help of printf and one or more loops) the desired
 * half-pyramids. Take care to left-align the bottom-left corner of the
 * left-hand half-pyramid
 */

#include <cs50.h>
#include <stdio.h>

// get pyramid height from user
int getPyramidHeight(void) {
  int height = 0;

  do {
    printf("Pyramid height (must be < 24): ");
    height = GetInt();
  } while(height > 23 || height < 0);

  return height;
}


int addSpaces(numSpaces) {
  for (int i = 0; i < numSpaces; i++) {
    printf(" ");
  }

  return 0;
}

int addHashes(numHashes) {
  for (int i = 0; i < numHashes; i++) {
    printf("#");
  }

  return 0;
}

int main(void) {
  int height = getPyramidHeight();
  int spaces = height - 1;

  for (int i = 1; i <= height; i++) {
    // first half
    addSpaces(spaces);
    addHashes(i + 1);
    printf("\n");

    // decrease indentation
    spaces--;
  }

  return 0;
}