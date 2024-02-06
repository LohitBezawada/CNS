#include <stdio.h>
#include <string.h>
#define MAX 26
void initializeMap(char map[MAX][MAX]) {
  for (int i = 0; i < MAX; i++) {
    for (int j = 0; j < MAX; j++) {
      map[i][j] = 'A' + (i + j) % MAX;
    }
  }
}
void encrypt(char map[MAX][MAX], char str[30], char key[20]) {
  int n, m;
  int keyLength = strlen(key);
  printf("\nEncrypted Text: ");
  for (int i = 0; i < strlen(str); i++) {
    n = m = 0;
    while (n + 'A' != str[i]) {
      n++;
    }
    while (m + 'A' != key[i % keyLength]) {
      m++;
    }
    printf("%c", map[n % MAX][m % MAX]);
  }
}
void decrypt(char map[MAX][MAX], char str[30], char key[20]) {
  int n, m;
  int keyLength = strlen(key);
  printf("\nDecrypted Text: ");
  for (int i = 0; i < strlen(str); i++) {
    n = m = 0;
    while (map[n % MAX][m % MAX] != str[i]) {
      n++;
    }
    while (m + 'A' != key[i % keyLength]) {
      m++;
    }
    printf("%c", 'A' + n % MAX);
  }
}
int main() {
  char map[MAX][MAX];
  initializeMap(map);
  char str[30], key[20];
  printf("Enter the plain text (in Upper case only): ");
  scanf("%s", str);
  printf("Enter the key value (in Upper case only): ");
  scanf("%s", key);
  encrypt(map, str, key);
  decrypt(map, str, key);
}
