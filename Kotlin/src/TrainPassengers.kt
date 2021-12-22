
fun main() {
    val startInfo = readLine()?.split(" ")
    val maks = startInfo?.get(0)!!.toInt(); var paaToget = 0.toLong()
    val antStasjoner = startInfo[1].toInt()
    var umulig = false
    var sisteVenting = 0.toLong()

    for (i in 0 until antStasjoner) {
        val info = readLine()!!.split(" ").map { it.toLong() }
        val forlot = info[0]; val gikkPaa = info[1]; val venter = info[2]
        val paaTogetEtterNye = paaToget + gikkPaa - forlot

        if (forlot > paaToget) {
            umulig = true
            break
        } else if (paaTogetEtterNye < 0) {
            umulig = true
            break
        } else if (paaTogetEtterNye > maks) {
            umulig = true
            break
        } else if (paaTogetEtterNye < maks && venter > 0) {
            umulig = true
            break
        }
        paaToget = paaTogetEtterNye
        sisteVenting = venter
    }
    if (umulig || paaToget > 0 || sisteVenting > 0) println("impossible") else println("possible")
}