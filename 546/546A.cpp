#include <iostream>
using namespace std;

int main(){
	int w,k,n,total=0;
	cin >> k >> n >> w;
	for(int i=1;i<=w;i++){
		total+=(i*k);
	}
	if (n<total){
		cout << total-n;
	}
	else{
		cout << 0;
	}
}
