/**
 * program that prompts a user for their name (using GetString to obtain their
 * name as a string) and then outputs their initials in uppercase with no spaces
 * or periods, followed by a newline (\n) and nothing more. You may assume that
 * the user’s input will contain only letters (uppercase and/or lowercase) plus
 * spaces. Folks like Joseph Gordon-Levitt, Conan O’Brien, and David J. Malan
 * won’t be using your program. But the user’s input might be sloppy, in which
 * case there might be one or more spaces at the start and/or end of the user’s
 * input or even multiple spaces in a row.
 */

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
  string name = GetString();
  int index = 0;

  // ignore whitespace, get first initial of name
  if (name[0] != ' ') {
    printf("%c", toupper(name[0]));
  } else {
    while (name[index] == ' ') {
      index++;
    }

    printf("%c", toupper(name[index]));
  }

  // ignore whitespace, get remaining initials
  for (int i = index, n = strlen(name); i < n; i++) {
    /**
     * check if the character that follows whitespace is a letter
     * ignore if last character of input string is a space
     */
    if (name[i] == ' ' && name[i + 1] != ' ' && i + 1 != strlen(name)) {
      printf("%c", toupper(name[i + 1]));
    }
  }

  printf("\n");
}