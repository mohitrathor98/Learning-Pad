/*
    Calculate average of all the elements in the array
*/

fun main(){
    print("Number of elements in the array: ")
    var sizeArray = Integer.valueOf(readLine())

    var numArray = arrayOf<Int>()
    for (index in 0..sizeArray-1){
        print("Element at index:: "+(index+1)+" ")
        numArray += Integer.valueOf(readLine())
    }

    var average = 0.0
    for (values in numArray){
        average += values
    }
    average /= sizeArray

    println("Average of array elements: "+average)
}