#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	int current,previous=0;
	int group=0,i;
	for(i=0;i<n;i++){
		cin >> current;
		if(current != previous){
			group++;
			previous=current;
		}
	}
	cout << group;
}
