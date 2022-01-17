
fun main() {
    val antKostymer = readLine()!!.toInt()
    val oversikt = HashMap<String, Int>()

    for (i in 0 until antKostymer) {
        val kostyme = readLine()!!
        oversikt[kostyme] = oversikt.getOrDefault(kostyme, 0) + 1
    }

    var minsteAntall = Int.MAX_VALUE
    val endeligListe = ArrayList<String>()
    for ((kostyme, antall) in oversikt) {
        if (antall < minsteAntall) {
            minsteAntall = antall
            endeligListe.clear()
            endeligListe.add(kostyme)
        } else if (antall == minsteAntall) {
            endeligListe.add(kostyme)
        }
    }
    for (kostyme in endeligListe.sorted()) {
        println(kostyme)
    }
}