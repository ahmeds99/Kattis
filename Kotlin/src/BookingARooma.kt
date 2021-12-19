import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    val oversikt = HashSet<String>()
    val antallRom = info[0].toInt(); val booked = info[1].toInt()

    for (i in 1..antallRom) oversikt.add("" + i)

    for (i in 1..booked) {
        val rom = tast.nextLine(); oversikt.remove(rom)
    }

    if (oversikt.isEmpty()) println("too late")
    else println(oversikt.first())
}