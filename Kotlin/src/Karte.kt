
fun main() {
    val info = readLine()!!
    val oversikt = HashSet<String>()
    var funnetDuplikat = false
    // Indicess are as follows: P, K, H, T
    val kortAntall = LinkedHashMap<Char, Int>()
    kortAntall['P'] = 13; kortAntall['K'] = 13; kortAntall['H'] = 13; kortAntall['T'] = 13

    for (i in info.indices step 3) {
        val kort = info.substring(i, i + 3)
        val type = info[i]
        if (oversikt.contains(kort)) {
            funnetDuplikat = true; break
        } else oversikt.add(kort)

        kortAntall[type] = kortAntall[type]!!.minus(1)
    }
    if (! funnetDuplikat)
        for ((_, ant) in kortAntall) print("$ant ")
    else println("GRESKA")
}