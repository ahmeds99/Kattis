import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val oversikt = hashSetOf<String>()

    val loggen = tast.nextLine().toInt()

    for (i in 1..loggen) {
        val info = tast.nextLine().split(" ")
        val kommando = info[0]; val navn = info[1]

        if (kommando == "entry") {
            var out = "$navn entered"
            if (oversikt.contains(navn)) {
                out += " (ANOMALY)"
            } else
                oversikt.add(navn)
            println(out)
        } else {
            var out = "$navn exited"
            if (! oversikt.contains(navn))
                out += " (ANOMALY)"
            else
                oversikt.remove(navn)
            println(out)
        }
    }
}