import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val frosh = tast.nextLine().toInt()
    val oversikt = HashMap<HashSet<String>, Int>()
    var antallLike = 1

    for (i in 0 until frosh) {
        val info = tast.nextLine().split(" ")
        val samling = HashSet<String>()

        for (tall in info) samling.add(tall)

        if (oversikt.containsKey(samling)) {
            val antall = oversikt[samling]
            if (antall != null) oversikt[samling] = antall + 1
        }
        else oversikt[samling] = 1

        if (oversikt[samling]!! > antallLike) antallLike++
    }

    if (antallLike == 1) println(frosh)
    else println(antallLike)
}