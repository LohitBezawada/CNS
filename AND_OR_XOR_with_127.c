#include<stdlib.h>
#include<string.h>
void main()
{
    char str[]="Hello World";
    char str1[12];
    char str2[12];
    char str3[12];
    int i,len;
    len = strlen(str);
    printf("AND each character with 127: ");
    for(i=0;i<len;i++)
    {
        str1[i] = str[i]&127;
        printf("%c",str1[i]);
        
    }
    printf("\n");
    printf("OR each character with 127: ");
    for(i=0;i<len;i++)
    {
        str2[i] = str[i]|127;
        printf("%c",str2[i]);
        
    }
    printf("\n");
    printf("XOR each character with 127: ");
    for(i=0;i<len;i++)
    {
        str3[i] = str[i]^127;
        printf("%c",str3[i]);
    }
    printf("\n");
}
