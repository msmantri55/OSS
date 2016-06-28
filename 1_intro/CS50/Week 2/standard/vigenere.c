/**
 * a program that encrypts messages using Vigenère’s cipher. This program must
 * accept a single command-line argument: a keyword, k, composed entirely of
 * alphabetical characters. If your program is executed without any command-line
 * arguments, with more than one command-line argument, or with one command-line
 * argument that contains any non-alphabetical character, your program should
 * complain and exit immediately, with main returning 1
 */

#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, string argv[]) {
  string keyword = " ";

  // check if user has supplied a key
  if (argc != 2) {
    printf("Usage: ./caesar <key>\n");
    return 1;
  } else {
    keyword = argv[1];

    // make sure keyword consists of letters only
    for (int i = 0, n = strlen(keyword); i < n; i++) {
      if (isalpha(keyword[i]) == 0) {
        printf("Keyword must only contain letters A-Z and a-z\n");
        return 1;
      }
    }
  }

  // convert keyword to lowercase
  for (int i = 0, n = strlen(keyword); i < n; i++) {
    keyword[i] = tolower(keyword[i]);
  }

  string plaintext = GetString();

  // for iterating across characters in keyword
  int counter = 0;

  for (int i = 0, n = strlen(plaintext); i < n; i++) {
    // check if current character is alphabetic
    if (isalpha(plaintext[i])) {
      if (64 < plaintext[i] && plaintext[i] < 91) {
        // capital letters
        if (plaintext[i] + keyword[counter % strlen(keyword)] > 90) {
          int output = plaintext[i] + keyword[counter % strlen(keyword)] - 65;

          // wrap text around alphabet if ASCII value > z
          if (output > 122) {
            output = 96 + output - 122;
          }

          printf("%c", toupper(output));
        } else {
          printf("%c", plaintext[i] + keyword[counter % strlen(keyword)]);
        }
      } else if (96 < plaintext[i] && plaintext[i] < 123) {
        // lowercase letters
        if (plaintext[i] + keyword[counter % strlen(keyword)] > 122) {
          int output = plaintext[i] + keyword[counter % strlen(keyword)] - 97;

          // wrap text around alphabet if ASCII value > z
          if (output > 122) {
            output = 96 + output - 122;
          }

          printf("%c", output);
        } else {
          printf("%c", plaintext[i] + keyword[counter % strlen(keyword)]);
        }
      }

      counter++;
    } else {
      // skip encryption on non-alphabetical characters
      printf("%c", plaintext[i]);
    }
  }

  printf("\n");
  return 0;
}