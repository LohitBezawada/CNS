#include<stdio.h>

int main() {
    unsigned int a[3][3] = { { 6, 24, 1 }, { 13, 16, 10 }, { 20, 17, 15 } };
    unsigned int b[3][3] = { { 8, 5, 10 }, { 21, 8, 21 }, { 21, 12, 8 } };
    int i, j;
    unsigned int c[3], d[3];
    char msg[20];
    int determinant = 0, t = 0;
    printf("Enter 3 character plain text (in Upper case only): ");
    scanf("%s", msg);
    for (i = 0; i < 3; i++) {
        c[i] = msg[i] - 'A';
        printf("%d ", c[i]);
    }
    for (i = 0; i < 3; i++) {
        t = 0;
        for (j = 0; j < 3; j++) {
            t += a[i][j] * c[j];
        }
        d[i] = t % 26;
    }
    printf("\nEncrypted Cipher Text: ");
    for (i = 0; i < 3; i++)
        printf("%c", d[i] + 'A');
    for (i = 0; i < 3; i++) {
        t = 0;
        for (j = 0; j < 3; j++) {
            t += b[i][j] * d[j];
        }
        c[i] = t % 26;
    }
    printf("\nDecrypted Cipher Text: ");
    for (i = 0; i < 3; i++)
        printf("%c", c[i] + 'A');
}
