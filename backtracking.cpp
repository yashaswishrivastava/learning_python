// print numbers from 1 to n and n to 1 using backtracking
#include<bits/stdc++.h>
using namespace std;

void printnumber(int i){
    if(i==0) return;

    cout<<i<<" ";
    printnumber(i-1);

}
int main(){
    int n;
    cout<<"enter the number";
    cin>>n;

    printnumber(n);
    return 0;
}

//another backtracking code
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