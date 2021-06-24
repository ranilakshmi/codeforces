#include<stdio.h>
int main(){
    int n,h;
    scanf("%d %d",&n,&h);
    int a;
    int max_width = n;
    for (int i=0;i<n;i++){
        scanf("%d",&a);
        if (a > h){
            max_width = max_width + 1;
        }
    }
    printf("%d",max_width);

}