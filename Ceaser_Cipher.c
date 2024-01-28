#include<stdio.h>
#include<string.h>
int main() {
  char plain[10], res[10];
  int key, i, n;
  printf("Enter the plain text: ");
  scanf("%s", plain);
  printf("Enter the key value: ");
  scanf("%d", & key);
  n = strlen(plain);
  printf("\nEncrypted Text: ");
  for (i = 0; i < n; i++) {
    res[i] = plain[i] + key;
    if ((plain[i] >= 'A' && plain[i] <= 'Z') && (res[i] > 'Z'))
      res[i] -= 26;
    else if ((plain[i] >= 'a' && plain[i] <= 'z') && (res[i] > 'z'))
      res[i] -= 26;
    printf("%c", res[i]);
  }
  printf("\nDecrypted Text: ");
  for (i = 0; i < n; i++) {
    plain[i] = res[i] - key;
    if ((res[i] >= 'A' && res[i] <= 'Z') && (plain[i] < 'A'))
      plain[i] += 26;
    else if ((res[i] >= 'a' && res[i] <= 'z') && (plain[i] < 'a'))
      plain[i] += 26;
    printf("%c", plain[i]);
  }
  printf("\n");
}
