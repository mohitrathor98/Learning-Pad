/*
    indexOfMax() function so that it returns the index of the largest element in the array,or null if array is empty
*/

fun indexOfMax(vararg arrayNum:Int): Int?{
    var arrayLen = arrayNum.size
    if(arrayLen == 0){
        return null
    } 

    var maxIndex = 0
    for(i in 1..arrayLen-1){
        if(arrayNum[maxIndex] < arrayNum[i]){
            maxIndex = i
        }
    }
    return maxIndex
}

fun main(){
    var arrNum = intArrayOf(5,3,2,1,4)
    var index = indexOfMax(*arrNum)
    println("Index of Maximum element: "+index)
}