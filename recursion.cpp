#include<bits/stdc++.h>
using namespace std;

void printnum(int i){
    if(i==0){
        return;
    }
    cout<<i<<" ";
    printnum(i-1);
}
int main(){
    printnum(7);
    return 0;
}