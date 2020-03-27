#include <stdio.h> // STandarD Input Output library

int main() { // Entry point
  printf("Size of data types in bytes:\n");
  printf("int: %d \n", sizeof(int));        // The size of an int in bytes
  printf("float: %d \n", sizeof(float));    // The size of a float in bytes
  printf("double: %d \n", sizeof(double));  // The size of a double in bytes
  printf("char: %d \n", sizeof(char));      // The size of a character in bytes

  return 0; // Return the 0 exit code
}
