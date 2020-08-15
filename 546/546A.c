#include <stdio.h>
int main(){
  int k,n,w,i,r;
  int p = 0;
  scanf("%d %d %d", &k, &n, &w);
  for (i=1;i<w+1;++i){
    p= p+(i*k);
  }
  if (n<p){
    r=(p-n);
  }
  else{
    r=0;
  }
  printf("%d",r);
  return 0;
}
