#include <math.h>
#include <stdio.h>
long long int power(long long int a, long long int b,
  long long int P) {
  if (b == 1)
    return a;
  else
    return (((long long int) pow(a, b)) % P);
}
int main() {
  long long int P, G, x, a, y, b, ka, kb;
  //P = 23
  printf("Enter the Value of P: ");
  scanf("%lld", & P);
  //G = 9;
  printf("Enter the Value of G: ");
  scanf("%lld", & G);
  //a = 4;
  printf("Enter the Private Key of A: ");
  scanf("%lld", & a);
  x = power(G, a, P);
  //b = 3; 
  printf("Enter the Private Key of B: ");
  scanf("%lld", & b);
  y = power(G, b, P);
  ka = power(y, a, P);
  kb = power(x, b, P);
  printf("Secret key for A is : %lld\n", ka);
  printf("Secret Key for B is : %lld\n", kb);
}
