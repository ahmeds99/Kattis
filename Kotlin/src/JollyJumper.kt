import java.io.IOException
import java.util.Scanner
import kotlin.math.abs

fun main() {
    val tast = Scanner(System.`in`)
    var linje = tast.nextLine()

    while (linje != "") {
        val info = linje.split(" ");
        val antTall = info[0].toInt()
        val oversikt = HashSet<String>()
        for (j in 1 until antTall) oversikt.add("" + j)

        for (j in 2 until info.size) {
            oversikt.remove("" + abs(info[j - 1].toInt() - info[j].toInt()))
        }
        if (oversikt.isEmpty()) println("Jolly")
        else println("Not jolly")

        linje = tast.nextLine()
    }
}