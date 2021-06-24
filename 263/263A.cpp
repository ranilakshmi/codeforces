#include<iostream>
#include<cstdlib>
using namespace std;
int main(){
    int i,j,a;
     i=0;
     j=0;
    while(i<5){
        while(j<5){
            cin >> a;
            if (a == 1){
                break;
            }
            j = j+1;
        }
        if (a == 1){
            break;
        }
        j=0;
        i = i + 1;
    }
    i = i +1;
    j = j+1;
    cout << abs(3-i) + abs(3-j);
}