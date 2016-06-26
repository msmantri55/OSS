/**
 * program that encrypts messages using Caesar’s cipher. Your program must
 * accept a single command-line argument: a non-negative integer
 * csubi = (psubi + k) % 26
 */

#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, string argv[]) {
  int k = 0;

  // check if user has supplied a key
  if (argc != 2) {
    printf("Usage: ./caesar <key>\n");
    return 1;
  } else {
    k = atoi(argv[1]);
    string plaintext = GetString();

    // help make sure encrypted string wraps from Z to A or from z to a
    if (k > 26) {
      k = k % 26;
    }

    for (int i = 0, n = strlen(plaintext); i < n; i++) {
      // check if character is alphabetic
      if (isalpha(plaintext[i])) {
        /**
         * a-z = 97-122, A-Z = 65-90
         */
        if (64 < plaintext[i] && plaintext[i] < 91) {
          // capital letters
          if (plaintext[i] + k > 90) {
            printf("%c", 64 + (plaintext[i] + k - 90));
          } else {
            printf("%c", plaintext[i] + k);
          }
        } else if (96 < plaintext[i] && plaintext[i] < 123) {
          // lowercase letters
          if (plaintext[i] + k > 122) {
            printf("%c", 96 + (plaintext[i] + k - 122));
          } else {
            printf("%c", plaintext[i] + k);
          }
        }
      } else {
        // print character if it is not an alphabetic character
        printf("%c", plaintext[i]);
      }
    }
  }

  printf("\n");
  return 0;
}