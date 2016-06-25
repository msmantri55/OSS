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