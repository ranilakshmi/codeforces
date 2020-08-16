#include<stdio.h>
#include<string.h>
int main(){
  int n;
  scanf("%d",&n);
  char str[n];
  scanf("%s",str);
  int o=0,z=0;
  for(int i=0;str[i]!='\0';i++){
    if (str[i]=='z'){
      z=z+1;
    }
    else if(str[i]=='n'){
      o=o+1;
    }
  }
  for (int i=1;i<o+1;i++){
    printf("1 ");
  }
  for (int i=1;i<z+1;i++){
    printf("0 ");
  }
}
