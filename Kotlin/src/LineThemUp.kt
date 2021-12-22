
fun main() {
    val antNavn = readLine()?.toInt()
    val liste = ArrayList<String>()

    for (i in 0 until antNavn!!) liste.add(readLine()!!)
    var increasing = true
    if (liste[0] > liste[1]) increasing = false

    if (increasing) {
        if (liste == liste.sorted()) println("INCREASING")
        else println("NEITHER")
    } else {
        if (liste == liste.sorted().reversed()) println("DECREASING")
        else println("NEITHER")
    }
}