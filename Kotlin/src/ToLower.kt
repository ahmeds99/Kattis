import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    var total = 0

    for (i in 1..info[0].toInt()) {
        var godkjent = true
        for (j in 1..info[1].toInt()) {
            val text = tast.nextLine()
            for (letter in text.substring(1)) {
                if (letter.isUpperCase()) godkjent = false
            }
        }
        if (godkjent) total++
    }
    println(total)
}