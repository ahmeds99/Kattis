fun main() {
    val antOverforinger = readLine()!!.toInt()
    var biggestDifference = 0
    var total = 0

    for (i in 0 until antOverforinger) {
        val transaction = readLine()!!.toInt()

        total += transaction
        if (total < biggestDifference) biggestDifference = total
    }
    println(biggestDifference * -1)
}