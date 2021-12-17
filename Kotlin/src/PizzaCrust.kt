import java.util.Scanner
import kotlin.math.pow

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    val skorpe = info[1].toDouble()
    val hele = info[0].toDouble()
    val resten = hele - skorpe

    println((resten.pow(2) * Math.PI / (hele.pow(2) * Math.PI)) * 100)
}