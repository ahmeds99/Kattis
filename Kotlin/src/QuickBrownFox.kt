
fun main() {
    val antCaser = readLine()?.toInt()

    for (i in 0 until antCaser!!) {
        var base = "abcdefghijklmnopqrstvwxyz"
        val setning = readLine()?.lowercase()

        if (setning != null) {
            for (c in setning) {
                if (c in base) base = base.replace(c.toString(), "")
            }
        }
        when (base) {
            "" -> println("pangram")
            else -> println("missing $base")
        }
    }
}