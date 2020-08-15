#include<stdio.h>
int main(){
    int a,b,c,t,i;
    scanf("%d", &t);
    int x=0;
    int y=0;
    int z=0;
    for (i=1;i<t+1;++i){
    scanf("%d %d %d", &a, &b, &c);
    x=x+a;
    y=y+b;
    z=z+c;
    }
    if (x==0 && y==0 && z==0){
        printf("YES");
    }
    else{
        printf("NO");
    }
 
    return 0;
}
