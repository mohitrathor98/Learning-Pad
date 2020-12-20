/*
    Months in words,on giving integers as inputs
*/

fun main(){
    print("Month Number: ")
    var monthNumber = Integer.valueOf(readLine())

    when(monthNumber){
        1-> println("January")
        2-> println("Febuary")
        3-> println("March")
        4-> println("April")
        5-> println("May")
        6-> println("June")
        7-> println("July")
        8-> println("August")
        9-> println("September")
        10-> println("October")
        11-> println("November")
        12-> println("December")
        else -> { 
            println("Not a month of year") 
        } 
    }
}