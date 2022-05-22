
fun main() {
    val info = readLine()!!.split(" ")
    val antallDommere = info[0].toInt()
    val harDomt = info[1].toInt()
    var minScore = (antallDommere - harDomt) * 3.0
    var maxScore = (antallDommere - harDomt) * -3.0

    for (i in 0 until harDomt) {
        val score = readLine()!!.toInt()
        minScore += score
        maxScore += score
    }

    println("${(maxScore / antallDommere)} ${(minScore / antallDommere)}")
}