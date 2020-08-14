#include <stdio.h>
int main(){
    int t,n;
    int i=1;
    scanf("%d", &t);
    for (i=1;i<t+1;++i){
        scanf("%d", &n);
        if (n<4){
            printf("%d\n",4-n);
        }
        else{
            if (n%2==1){
                printf("1\n");
            }
            else{
                printf("0\n");}
            }
       }
    return 0;
}
