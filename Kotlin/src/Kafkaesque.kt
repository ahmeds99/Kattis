fun main() {
    val antTall = readLine()!!.toInt()
    var forrige = 0
    var antallPasseringer = 1

    for (i in 0 until antTall) {
        val naavarende = readLine()!!.toInt()

        if (naavarende < forrige)
            antallPasseringer++

        forrige = naavarende
    }
    println(antallPasseringer)
}