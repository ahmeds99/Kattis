
fun main() {
    val antCaser = readLine()!!.toInt()

    for (i in 0 until antCaser) {
        val info = readLine()!!
        if (info == "P=NP") println("skipped")
        else {
            val biter = info.split("+")
            println(biter[0].toInt() + biter[1].toInt())
        }
    }
}