#include <stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	for (i=1;i<n;i++){
		if (i%2==1){
			printf("I hate that ");
		}
		else{
			printf("I love that ");
		}
	}	
	if (n%2==1){
		printf("I hate it ");
	}
	else{
		printf("I love it");
	}
}
