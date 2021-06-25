#include<iostream>
using namespace std;
int main(){
    int t,w,h,n,p,a;
    cin >> t;
    for(int i=0;i<t;i++){
        n = 1;
        cin >> w >> h >> p;
        a = w*h;
        while (a%2==0){
            n = 2 * n;
            a = a/2;
        }
        if (n>=p){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
    }
}
