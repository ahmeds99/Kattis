fun main() {
    val info = readLine()!!
    var aliceScore = 0
    var barbScore = 0
    var winByTwo = false
    var scoreTo = ""

    for (i in info.indices) {
        if (info[i] == 'A') scoreTo = "A"
        else if (info[i] == 'B') scoreTo = "B"
        else if (scoreTo == "A") aliceScore += (info[i] + "").toInt()
        else if (scoreTo == "B") barbScore += (info[i] + "").toInt()

        if (aliceScore == 10 && barbScore == 10) winByTwo = true

        if (! winByTwo) {
            if (aliceScore >= 11) {
                println("A")
                break
            } else if (barbScore >= 11) {
                println("B")
                break
            }
        } else {
            if (aliceScore - barbScore > 1) {
                println("A")
                break
            } else if (barbScore - aliceScore > 1) {
                println("B")
                break
            }
        }
    }
}