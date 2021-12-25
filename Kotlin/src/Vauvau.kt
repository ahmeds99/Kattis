
fun main() {
    val info = readLine()!!.split(" ").map { it.toInt() }
    val hundA = HashSet<Int>(); var startA = 1
    val hundB = HashSet<Int>(); var startB = 1

    while (startA < 999) {
        for (i in 0 until info[0]) {
            hundA.add(startA)
            startA += 1
        }
        startA += info[1]
    }
    while (startB < 999) {
        for (i in 0 until info[2]) {
            hundB.add(startB)
            startB += 1
        }
        startB += info[3]
    }

    val helter = readLine()!!.split(" ").map { it.toInt() }
    for (helt in helter) {
        var antAngrep = 0
        if (helt in hundA) antAngrep++
        if (helt in hundB) antAngrep++

        when (antAngrep) {
            0 -> println("none")
            1 -> println("one")
            else -> println("both")
        }
    }
}