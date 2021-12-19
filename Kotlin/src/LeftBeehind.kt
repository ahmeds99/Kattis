import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    var linje = tast.nextLine().split(" ")
    while (!(linje[0] == "0" && linje[1] == "0")) {
        val info = linje.map { it.toInt() }
        if (info[0] + info[1] == 13) println("Never speak again.")
        else if (info[0] > info[1]) println("To the convention.")
        else if (info[0] < info[1]) println("Left beehind.")
        else println("Undecided.")

        linje = tast.nextLine().split(" ")
    }
}