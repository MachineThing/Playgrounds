#include <stdio.h> // STandarD Input Output library

int main() { // Entry point
  int numa, numb;

  printf("Type in a number please!\n");
  scanf("%d", &numa);
  printf("Another number please!\n");
  scanf("%d", &numb);

  printf("%d plus %d equals %d!\n", numa, numb, numa+numb);
  return 0;
}
