#include <stdio.h> // STandarD Input Output library

int main() { // Entry point
  const int nameMax = 25;

  printf("What is your name? (%d characters max)\nName: ", nameMax);
  char name[nameMax]; // An empty character array
  gets(name); // Get input from user and then put it into the array
  printf("Hello there %s! Nice to meet you!", name); // Print the user's name
  return 0; // Return the 0 exit code
}
