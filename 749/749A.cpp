#include <iostream>
using namespace std;

int main(){
	int k;
	cin >> k;
	int i;
	cout << k/2 ;
	cout << "\n";
	for (i=1;i<(k/2);i++){
		cout << "2 ";
	}
	if (k%2==0){
		cout << 2 ;
	}
	else{
		cout << 3;
	}
}
