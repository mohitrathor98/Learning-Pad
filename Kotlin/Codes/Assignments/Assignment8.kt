/*
    Calculate difference between two time periods where Time is a user defined class
*/

class Time(internal var hours:Int,internal var minutes:Int,internal var seconds:Int){

    fun timeFormat():String{
        return this.hours.toString()+":"+this.minutes.toString()+":"+this.seconds.toString()
    }
}

fun difference(startTime:Time,endTime:Time) : Time{
    var diffTime = Time(0,0,0)

    var sec = endTime.seconds - startTime.seconds
    if(sec < 0){
        diffTime.minutes -= 1
        diffTime.seconds = 60+sec
    } else {
        diffTime.seconds = sec
    }

    var min = endTime.minutes - startTime.minutes
    if(min<0){
        diffTime.hours -= 1
        diffTime.minutes += (60+min)
    } else {
        diffTime.minutes += min
    }

    var hr = endTime.hours - startTime.hours
    if(hr<0){
        diffTime.hours += (24+hr)
    } else {
        diffTime.hours += hr
    }
    return diffTime    
}

fun main(){
    var startTime = Time(22,22,22)
    var endTime = Time(4, 2, 12)

    var diffTime = difference(startTime,endTime)

    println("Start Time: "+startTime.timeFormat()+"\nEnd Time: "+endTime.timeFormat()+"\nTime difference: "+diffTime.timeFormat())
}