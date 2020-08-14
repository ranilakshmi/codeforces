#include<stdio.h>
int main(){
    int n,x=0,r=0,i,y=0;
    scanf("%d",&n);
    for (i=0;i<n;i++){
        scanf("%d",&x);
        if(x!=y){
            r=r+1;
        }
        y=x;
    }
    printf("%d",r);
}
