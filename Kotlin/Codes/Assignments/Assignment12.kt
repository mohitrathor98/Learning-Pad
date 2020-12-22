/*
    function to check string palindrome
*/

fun palindrome(str:String): Boolean{
    var strLen = str.length

    var i = 0
    while(i != (strLen/2)){
        if(str[i] != str[strLen-i-1]){
            return false
        }
        i++
    }

    return true
}

fun main(){
    print("String: ")
    var str = readLine().toString()

    if(palindrome(str)){
        println(str+" is a palindrome")
    } else {
        println(str+" is not a palindrome")
    }
}