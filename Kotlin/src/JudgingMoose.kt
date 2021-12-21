import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val left = tast.nextInt(); val right = tast.nextInt()

    if (left == 0 && right == 0) println("Not a moose")
    else if (left == right) println("Even ${left + right}")
    else {
        val highest = if (left > right) left else right
        println("Odd ${highest * 2}")
    }
}