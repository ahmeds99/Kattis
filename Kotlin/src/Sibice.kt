import kotlin.math.sqrt

fun main() {
    val info = readLine()!!.split(" ")
    val pytagoras = sqrt((info[1].toInt() * info[1].toInt() + info[2].toInt() * info[2].toInt()).toDouble())

    for (i in 0 until info[0].toInt()) {
        if (readLine()!!.toDouble() > pytagoras)
            println("NE")
        else
            println("DA")
    }
}