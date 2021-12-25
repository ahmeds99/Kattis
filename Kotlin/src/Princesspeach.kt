fun main() {
    val info = readLine()!!.split(" ")
    val oversikt = HashSet<String>()
    for (i in 0 until info[1].toInt()) oversikt.add(readLine()!!)

    for (i in 0 until info[0].toInt()) {
        if (! oversikt.contains(i.toString())) println(i)
    }
    println("Mario got ${oversikt.size} of the dangerous obstacles.")
}