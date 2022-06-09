fun main() {
    val info = readLine()!!.split(" ").map { it.toInt() }
    val limit = info[0]
    var antallInne = 0
    var antallUtelatt = 0

    for (i in 0 until info[1]) {
        val handling = readLine()!!.split(" ")

        if (handling[0] == "enter" && handling[1].toInt() + antallInne > limit)
            antallUtelatt++

        else if (handling[0] == "enter")
            antallInne += handling[1].toInt()

        else
            antallInne -= handling[1].toInt()
    }
    println(antallUtelatt)
}