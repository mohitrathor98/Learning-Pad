#include<bits/stdc++.h>


bool palindrome(std::string str,int strLen,int index = 0){
    if(index == (strLen/2)){
        return true;
    } 

    if(str[index] != str[strLen-index-1]){
        return false;
    }

    return palindrome(str,strLen,index+1);
}

int main(){
    std::string str;
    std::cout<<"Enter a string: ";
    std::cin>>str; 

    if(palindrome(str,str.length())){
        std::cout<<"String "<<str<<" is a palindrome"<<std::endl;
    } else {
        std::cout<<"String "<<str<<" is not a palindrome"<<std::endl;
    }
}