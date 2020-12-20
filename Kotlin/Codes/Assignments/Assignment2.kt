/*
    calculate sum of natural numbers using recursion
*/

fun addNumbers(number:Int = 20) : Int{
    if(number == 0){
        return 0
    }

    return number+ addNumbers(number-1) 
}

fun main(){

    print("Limit(if 0 passed, default limit will be taken): ")
    var number = Integer.valueOf(readLine())
    if(number != 0){
        println("Sum of "+number+" natural numbers: "+addNumbers(number))
    } else {
        println("Sum of "+number+" natural numbers: "+addNumbers())
    }
}