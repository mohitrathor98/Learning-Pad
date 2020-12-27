#include<bits/stdc++.h>
using namespace std;

void printSubset(string str,string current = " ",int index = 0){
    if(index == str.length()){
        cout<<current<<" ";
        return;
    }

    printSubset(str,current,index+1);
    printSubset(str,current+str[index],index+1);

}

int main(){
    string str;
    cout<<"Enter string: ";
    cin>>str;

    cout<<"Subset of str:\n";
    printSubset(str);
    cout<<endl;
}