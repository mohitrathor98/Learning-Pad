/*
    Factroial of given number
*/

fun main(){
    print("Number: ")
    var number = Integer.valueOf(readLine())

    if(number < 0){
        println("Negative numbers don't have valid factorials")
        return
    } 

    var fac:Int = 1
    for (values in 2..number){
        fac *= values
    }

    println("Factorial of "+number+" is:: "+fac)
}