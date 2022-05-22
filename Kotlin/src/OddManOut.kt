fun main() {
    val antCaser = readLine()!!.toInt()

    for (i in 0 until antCaser) {
        readLine()
        val info = readLine()!!.split(" ")
        val finnAleneGjesten = hashSetOf<String>()

        for (gjest in info) {
            if (gjest in finnAleneGjesten) finnAleneGjesten.remove(gjest)
            else finnAleneGjesten.add(gjest)
        }
        println("Case #${i + 1}: " + finnAleneGjesten.first())
    }
}