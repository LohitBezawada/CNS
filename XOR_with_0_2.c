#include <stdio.h>
#include <string.h>
void binaryValue(int n) {
  int b[8], x[8];
  int j, k, l;
  for (j = 7; j >= 0; j--) {
    b[j] = n % 2;
    n = n / 2;
  }
  for (k = 0; k < 8; k++) {
    if (b[k] == 0) {
      x[k] = 0;
    } else {
      x[k] = 1;
    }
  }
  int decimal = 0;
  for (l = 0; l < 8; l++) {
    decimal = decimal * 2 + x[l];
  }
  printf("%c", (char) decimal);
}
int main() {
  int i;
  char str[]="Hello World";
  printf("After XOR operation:\n");
  for (i = 0; i < strlen(str); i++) {
    binaryValue((int) str[i]);
  }
}
