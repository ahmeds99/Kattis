import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val antTall = tast.nextLine().toInt()
    val tallene = tast.nextLine().split(" ")

    var forrige = Int.MIN_VALUE; var antallTårn = 0

    for (tall in tallene) {
        if (tall.toInt() > forrige) {
            antallTårn++
        }
        forrige = tall.toInt()
    }
    println(antallTårn)
}