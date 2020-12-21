/*
    Calculate difference between two time periods where Time is a user defined class
*/

class Time(internal var hours:Int,internal var minutes:Int,internal var seconds:Int){
}

fun difference(startTime:Time,endTime:Time) : String{
    var diffTime = Time(0,0,0)

    var sec = endTime.seconds - startTime.seconds
    


    return diffTime.hours.toString()+":"+diffTime.minutes.toString()+":"+diffTime.seconds.toString()
}

fun main(){
    var startTime = Time(22,22,22)
    var endTime = Time(23, 50, 12)

    var diff = difference(startTime,endTime)

    println("Start Time: 22:22:22\nEnd Time: 23:50:12\nTime difference: "+diff)
}