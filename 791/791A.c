#include <stdio.h>
int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    int i = 1;
 
    while (a<=b)
    {
        a=a*3;
        b=b*2;
        ++i;
    }
 
    printf("%d", i-1);
    return 0;
}
