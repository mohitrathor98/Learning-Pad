/*
    Tuple & Destructuring declaration
*/

class Player(var runs:Int,var age:Int, var nom:Int, var name:String, var player_number:Int){
    fun findPlayerDetails(playerNum:Int) : Pair<Int,Player>{
        
    }
}

fun main(){
    var playerObj1 = Player(199, 22, 10, "Rishabh", 20)
    var playerObj2 = Player(183, 32, 223, "Virat", 18)
    var playerObj3 = Player(183, 40, 400, "Mahendra", 7)
    var playerObj4 = Player(200, 42, 500, "Sachin", 10)
    var listOfPlayers = arrayListOf(playerObj1,playerObj2,playerObj3,playerObj4)
}