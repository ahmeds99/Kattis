fun main() {
    val numOfTeams = readLine()!!.toInt()
    val winners = mutableListOf<String>()
    val hashMap = hashMapOf<String, String>()

    for (i in 0 until numOfTeams) {
        val info = readLine()!!
        val parts = info.split(" ")
        val uni = parts[0]
        val team = parts[1]

        if (uni !in hashMap) {
            hashMap[uni] = team
            if (winners.size < 12)
                winners.add(info)
        }
    }
    for (winner in winners) println(winner)
}