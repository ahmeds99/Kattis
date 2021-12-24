
fun main() {
    val tekst = readLine()
    val lengde = tekst!!.length
    val oversikt = HashMap<String, Int>()

    for (i in 0 until lengde step lengde / 3) {
        val ord = tekst.substring(i, i + lengde / 3)
        if (! oversikt.containsKey(ord)) oversikt[ord] = 1
        else oversikt[ord] = oversikt[ord]!! + 1
    }
    for ((ord, antall) in oversikt) if (antall > 1) println(ord)
}