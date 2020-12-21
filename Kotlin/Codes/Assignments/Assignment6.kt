/*
    Print result of the following operations
    a. -5+8*6
    b. (55+9)%9
    c. 20+ -3*5 /8
    d. 5+15/3*2-8%3
*/

fun main(){
    var a = -5+8*6
    var b = (55+9)%9
    var c = 20+ -3*5 /8 // first multiply then divide and at last add
    var d = 5+15/3*2-8%3 // first divide-->multiply-->modulo-->add and then substract

    println("-5+8*6 = "+a+"\n(55+9)%9 = "+b+"\n20+ -3*5/8 = "+c+"\n5+15/3*2-8%3 = "+d)
}