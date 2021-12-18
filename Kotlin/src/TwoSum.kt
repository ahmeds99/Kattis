import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val info = tast.nextLine().split(" ")
    println(info[0].toInt() + info[1].toInt())
}