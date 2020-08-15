#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int n,m,k;
	cin >> n;
	cin >> m;
	cin >> k;
	vector <int> holes(m);
	for(auto &it:holes)cin >> it;
	sort(holes.begin(),holes.end());
	int swap=0,bone_in_hole=0;
	int p1,p2,p=1;
	if (holes[0]==1){
		cout << 1;
		bone_in_hole=1;
	}
		
	while (swap<k && bone_in_hole==0){
		swap++;
		cin >> p1;
		cin >> p2;
		if (p1==p){
			p=p2;
		}
		else{
			if(p2==p){
				p=p1;
			}
		}
		if (binary_search(holes.begin(),holes.end(),p)){
			bone_in_hole=1;
			cout << p;
		}
	}
	if (bone_in_hole==0){
		cout << p;
	}
}
