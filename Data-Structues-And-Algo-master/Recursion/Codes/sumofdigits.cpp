#include<bits/stdc++.h>
using std::cout;
using std::cin;
using std::endl;

int sumofdigits(int num){
    if(num == 0){
        return 0;
    }

    return num%10 + sumofdigits(num/10);
}

int main(){
    int num;
    cout<<"Number: ";
    cin>>num;

    cout<<"Sum of digits of "<<num<<" is "<<sumofdigits(num)<<endl;
}