/**
 * write a program that prompts the user for a credit card number and then
 * reports (via printf) whether it is a valid American Express, MasterCard, or
 * Visa card number, per the definitions of each’s format herein. So that we can
 * automate some tests of your code, we ask that your program’s last line of
 * output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more,
 * nothing less, and that main always return 0. For simplicity, you may assume
 * that the user’s input will be entirely numeric (i.e., devoid of hyphens, as
 * might be printed on an actual card). But do not assume that the user’s input
 * will fit in an int!
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int cardChecker(long long number) {
  long long ccNum = number;
  int numDigits = 0;

  // calculate number of digits in CC number
  while (ccNum > 0) {
    ccNum = ccNum / 10;
    numDigits++;
  }

  // declare array of `numDigits` digits
  int digit[numDigits];

  // reset ccNum
  ccNum = number;
  for (int i = numDigits - 1; i >= 0; i--) {
    // set element at location i to last digit of ccNum
    digit[i] = ccNum % 10;

    // shorten ccNum
    ccNum = ccNum / 10;
  }

  string cardType = "";

  /**
   * validate card type
   *
   * (15 digits) AMEX numbers start with 34 or 37
   * (16 digits) MASTERCARD numbers all start with 51, 52, 53, 54, or 55
   * (13 and 16 digits) VISA numbers all start with 4
   */
  if (numDigits == 15 && digit[0] == 3 && (digit[1] == 4 || digit[1] == 7)) {
    cardType = "AMEX";
    // declare arrays separating odd and even digits
    int numEvens = 0;
    int even[numDigits];
    int numOdds = 0;
    int odd[numDigits];

    // populate arrays of even and odd digits
    for (int i = 0; i < numDigits; i++) {
      if ((i + 1) % 2 == 0) {
        numEvens++;
        even[numEvens] = digit[i];
      } else {
        numOdds++;
        odd[numOdds] = digit[i];
      }
    }

    // add the digits of each even digit multiplied by 2
    int sumEvens = 0;
    for (int i = 1; i <= numEvens; i++) {
      // check if product has multiple digits
      if (even[i] * 2 > 9) {
        int doubled = even[i] * 2;
        while (doubled > 0) {
          sumEvens += doubled % 10;
          doubled = doubled / 10;
        }
      } else {
        sumEvens += even[i] * 2;
      }
    }

    // find the sum of each odd digit
    int sumOdds = 0;
    for (int i = 1; i <= numOdds; i++) {
      sumOdds += odd[i];
    }

    // check if last digit of sum is 0
    if ((sumEvens + sumOdds) % 10 != 0) {
      cardType = "null";
    }
  } else if ((numDigits == 13 || numDigits == 16) && digit[0] == 4) {
    cardType = "VISA";
  } else if (numDigits == 16 && digit[0] == 5 && (digit[1] == 1 || digit[1] == 2 || digit[1] == 3 || digit[1] == 4 || digit[1] == 5)) {
    cardType = "MASTERCARD";
  } else {
    cardType = "null";
  }

  // check if cardType is not equal to "null"
  if (strcmp(cardType, "null") != 0) {
    printf("%s\n", cardType);
  } else {
    printf("INVALID\n");
  }

  return 0;
}

int main(void) {
  // prompt user for CC number
  printf("Number: ");
  long long number = GetLongLong();

  // validate CC number
  cardChecker(number);
  return 0;
}