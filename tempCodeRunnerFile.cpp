#include<bits/stdc++.h>
using namespace std;

void numbers(int i, int n){
    if(i>n) return;

    numbers(i+1,n);
    cout<<i<<" ";


}
int main(){
    int n;
    cout<<"enter the number";
    cin>>n;
    numbers(1,n);
    return 0;
}