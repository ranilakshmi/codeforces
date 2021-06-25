#include<iostream>
#include<string>
using namespace std;
int main(){
    int n;
    string x,y;
    int a=1;
    int b=0;
    cin >> n;
    cin >> x;
    string team;
    for (int i=1;i<n;i++){
        cin >> team;
        if (team == x){
            a = a+1;
        }
        else{
            y=team;
            b=b+1;
        }
    }
    if(a>b){
        cout << x;
    }
    else{
        cout << y;
    }
}