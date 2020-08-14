#include<stdio.h>
int main(){
    int n,x,i;
    scanf("%d",&n);
    if (n%2==0){
        x=n/2;
        printf("%d\n",x);
        for (i=1;i<=x;i++){
            printf("2 ");
        }
    }
    if (n%2==1){
        x=n/2-1;
        printf("%d\n",x+1);
        for (i=1;i<=x;i++){
            printf("2 ");
        }
        printf("3");
}
}
