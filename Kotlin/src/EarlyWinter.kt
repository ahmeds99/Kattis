import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    val minste = info[1].toInt()

    val tidligeVintre = tast.nextLine().split(" ").map{ it.toInt() }
    var skrevetUt = false; var teller = 0

    while (! skrevetUt && teller < tidligeVintre.size) {
        if (tidligeVintre[teller] <= minste) {
            println("It hadn't snowed this early in $teller years!")
            skrevetUt = true
        }
        teller++
    }
    if (! skrevetUt) println("It had never snowed this early!")
}