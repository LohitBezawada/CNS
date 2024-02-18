#include <stdio.h>
#include <string.h>
#define SIZE 30
void getKeyMatrix(char * key, int keyMatrix[3][3]) {
  int k = 0;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      keyMatrix[i][j] = (key[k]) % 65;
      k++;
    }
  }
}
void encrypt(int cipherMatrix[3][1], int keyMatrix[3][3], int messageVector[3][1]) {
  int x, i, j;
  for (i = 0; i < 3; i++) {
    for (j = 0; j < 1; j++) {
      cipherMatrix[i][j] = 0;
      for (x = 0; x < 3; x++) {
        cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j];
      }
      cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
    }
  }
}
void HillCipher(char * message, char * key) {
  int keyMatrix[3][3];
  getKeyMatrix(key, keyMatrix);
  int messageVector[3][1];
  for (int i = 0; i < 3; i++)
    messageVector[i][0] = (message[i]) % 65;
  int cipherMatrix[3][1];
  encrypt(cipherMatrix, keyMatrix, messageVector);
  printf("Ciphertext: ");
  for (int i = 0; i < 3; i++)
    printf("%c", cipherMatrix[i][0] + 65);
  printf("\n");
}
int main() {
  char message[SIZE], key[SIZE];
  printf("Enter the plain text: ");
  fgets(message, SIZE, stdin);
  message[strcspn(message, "\n")] = '\0';
  printf("Enter the key value: ");
  fgets(key, SIZE, stdin);
  key[strcspn(key, "\n")] = '\0';
  HillCipher(message, key);
}
