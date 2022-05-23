fun main() {
    val info = readLine()!!
    val tall = info.toInt()

    if (tall < 149)
        println(99)
    else {
        val lastTwo = (info[info.length - 2] + "" + info[info.length - 1])
        if (lastTwo.toInt() >= 49) {
            println(tall + (99 - lastTwo.toInt()))
        } else
            println(tall - (lastTwo.toInt() + 1))
    }
}