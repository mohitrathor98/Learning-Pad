/*
    Number of "runs" of equal numbers
*/

fun runs(vararg arr:Int) : Int{
    
    if(arr.size == 0){
        return 0
    }
    var numRuns = 1
    var prevElement = arr[0]

    for(element in arr){
        if(element != prevElement){
            numRuns++
            prevElement = element
        }
    }

    return numRuns
}

fun main(){
    print("Size of Array: ")
    var sizeArray = Integer.valueOf(readLine())

    var array = intArrayOf()
    for(i in 0..sizeArray-1){
        print("Element at index "+i+": ")
        array += Integer.valueOf(readLine())
    }

    var numRuns = runs(*array)
    println("Number of runs in the given array is "+numRuns)
}