/*
    Calculate LCM using while loop and if statements
 */
fun main(){

    print("Two space seperated numbers:: ")
    var (firstNum,secondNum) = readLine()!!.split(' ').map(String::toInt)

    var highNum:Int
    if(firstNum > secondNum){
        highNum = firstNum
    } else {
        highNum = secondNum
    }

    while(true){
        if ((highNum % firstNum == 0) && (highNum%secondNum == 0)){
            println("LCM of "+ firstNum +" and "+ secondNum +" is "+highNum)
            break
        }
        highNum++
    }
}