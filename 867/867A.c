#include <stdio.h>
int main(){
int n,i,s=0,f=0;
scanf("%d",&n);
char travel[n];
scanf("%s",travel);
for (i=0;i<n-1;i++){
	if (travel[i]=='S' && travel[i+1]=='F'){
		s=s+1;
	}
	else if (travel[i]=='F' && travel[i+1]=='S'){
		f=f+1;
	}
}
if (s>f){
	printf("YES");
}
else{
	printf("NO");
}
}
