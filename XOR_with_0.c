#include<stdlib.h>
#include<string.h>
void main()
{
    char str[]="Hello World";
    char res[11];
    int i,len;
    len=strlen(str);
    for(i=0;i<len;i++)
    {
        res[i]=str[i]^0;
        printf("%c",res[i]);
    }
    printf("\n");
}
