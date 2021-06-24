#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
int main(){
    priority_queue <int,vector<int>,greater<int>> pq;
    int n,a;
    cin >> n;
    for (int i =0;i<n;i++){
        cin >> a;
        pq.push(a);
    }
    while(!pq.empty()){
        cout << pq.top() << " ";
        pq.pop();
    }
}