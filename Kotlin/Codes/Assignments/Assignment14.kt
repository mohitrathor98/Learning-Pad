/*
    Lambda function which filters all the even number for the input list<Int>
*/

val evenSeperate:(arr:List<Int>) -> List<Int> = {arr -> arr.filter{it%2 == 0}} 

fun main(){
    var arrayList = listOf(1,2,3,4,5,6,7,8,9,10)
    println("Given array:: "+arrayList)
    println("Filtered array:: "+evenSeperate(arrayList))
}