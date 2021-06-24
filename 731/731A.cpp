#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;
int main(){
    string word;
    cin >> word;
    int total_rotation = min(abs(word[0] - 'a'),abs(26 - (word[0] - 'a')));
    int rotation;
    for (int i=1;i<word.size();i++){
        rotation = abs(word[i-1] - word[i]);
        if (rotation <= 13){
            total_rotation = total_rotation + rotation;
        }
        else{
            total_rotation = total_rotation + 26 - rotation;
        }
    }
    cout << total_rotation;
}