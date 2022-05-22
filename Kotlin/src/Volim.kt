fun main() {
    var spiller = readLine()!!.toInt()
    val antSpm = readLine()!!.toInt()
    var tid = 0

    for (i in 0 until antSpm) {
        val info = readLine()!!.split(" ")
        val tidForSpm = info[0].toInt()
        val svar = info[1]

        if ((tidForSpm + tid) >= 210) {
            println(spiller)
            break
        }
        if (svar == "T") spiller += 1
        if (spiller > 8) spiller = 1

        tid += tidForSpm
    }
}