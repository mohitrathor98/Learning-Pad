/*
    Transpose of a matrix
*/

fun main(){
    var arr = arrayOf(arrayOf(1,2,3),arrayOf(4,5,6),arrayOf(7,8,9))

    println("Before Transposing::")
    for(row in arr){
        for(col in row){
            print(""+col+" ")
        }
        println()
    }

    println("After Transposing::")
    for(row in 0..2){
        for(col in 0..2){
            print(""+arr[col][row]+" ")
        }
        println()
    }
}