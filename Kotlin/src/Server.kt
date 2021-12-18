import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    val maksTid = info[1].toInt(); var total = 0
    var fullfoerteOppgaver = 0

    for (tall in tast.nextLine().split(" ")) {
        if (tall.toInt() + total > maksTid) {
            break
        }
        total += tall.toInt(); fullfoerteOppgaver++
    }
    println(fullfoerteOppgaver)
}