#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 20
int main() {
    int i;
    char str[MAX], str1[MAX], str2[MAX];
    char alpha[27] = "abcdefghijklmnopqrstuvwxyz";
    printf("\nPlain  Alphabets: %s", alpha);
    srand(time(NULL));
    for (i = 25; i > 0; i--) {
        int j = rand() % (i + 1);
        char temp = alpha[i];
        alpha[i] = alpha[j];
        alpha[j] = temp;
    }
    printf("\nCipher Alphabets: %s", alpha);
    printf("\nEnter String: ");
    gets(str);
    // Encryption
    for (i = 0; str[i]; i++) {
        if (islower(str[i])) {
            str1[i] = alpha[str[i] - 'a'];
        } else {
            str1[i] = str[i];
        }
    }
    str1[i] = '\0';
    // Decryption
    for (i = 0; str1[i]; i++) {
        char currentChar = str1[i];
        int index = 0;
        while (alpha[index] != currentChar) {
            index++;
        }
        str2[i] = 'a' + index;
    }
    str2[i] = '\0';
    printf("\nEncrypted String: %s", str1);
    printf("\nDecrypted String: %s\n", str2);
}
