fun main() {
    var most = 0; var winner = ""
    for (i in 1..5) {
        val info = readLine()!!.split(" ").map { it.toInt() }
        val sum = info.sum()
        if (sum > most) {
            most = sum
            winner = i.toString()
        }
    }
    println("$winner $most")
}