/*
    Greatest number in the array
*/

fun main(){
    print("Size of array: ")
    var sizeArray = Integer.valueOf(readLine())

    var array = arrayOf<Int>()
    for (index in 0..sizeArray-1){
        print("Element at Index "+(index+1)+": ")
        array += Integer.valueOf(readLine())
    }

    var largest = array[0]
    for(index in 1..sizeArray-1){
        if(largest < array[index]){
            largest = array[index]
        }
    }

    println("Largest number in the array is "+largest)
}