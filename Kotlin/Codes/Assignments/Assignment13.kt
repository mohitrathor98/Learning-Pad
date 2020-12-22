/*
    sum, diff, multiplication, division taking operator as argument
*/

fun add(a:Int,b:Int){
    println("Sum of "+a+" and "+b+" is "+(a+b))
}

fun sub(a:Int,b:Int){
    println("Difference between "+a+" and "+b+" is "+(a-b))
}

fun mul(a:Int,b:Int){
    println("Product of "+a+" and "+b+" is "+(a*b))
}

fun div(a:Int,b:Int){
    if(b == 0){
        println("can't divide when b is 0")
        return
    }
    println("Division of "+a+" and "+b+" is "+(a/b))
}

fun main(sArgs:Array<String>){
    if(sArgs.size == 0){
        println("An operator is required as an argument")
        return
    }

    print("Give two numbers::\na = ")
    var a = Integer.valueOf(readLine())
    print("b = ")
    var b = Integer.valueOf(readLine())

    when(sArgs[0]){
        "+" -> add(a,b)
        "-" -> sub(a,b)
        "*" -> mul(a,b)
        "/" -> div(a,b)
        else -> println(
            "Invalid Argument. Give any one: +,-,*,/"        
        )
    }

}