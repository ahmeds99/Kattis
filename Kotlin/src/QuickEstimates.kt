import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val antCaser = tast.nextInt()
    for (i in 0 until antCaser) println(tast.next().length)
}