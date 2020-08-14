#include <stdio.h>
int main()
{
  int weight;
  scanf("%d", &weight);
  if (weight%2 == 1){
    printf("No");
  }
  else {
    if (weight == 2){
      printf("No");
    }
    else{
      printf("Yes");
    }
  }
  return 0;
}
