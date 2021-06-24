#include<iostream>
using namespace std;
int main(){
    int n,h,a;
    cin >> n >> h;
    int max_width = n;
    for (int i=0;i<n;i++){
        cin >> a;
        if (a>h){
            max_width = max_width + 1;
        }
    }
    cout << max_width;
}