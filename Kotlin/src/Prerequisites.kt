fun main() {
    var info = readLine()!!.split(" ")

    while (info[0] != "0") {
        val antKataloger = info[1].toInt()
        val freddiesKurs = HashSet(readLine()!!.split(" "))
        val oversikt = HashMap<String, Kategori>()

        for (i in 0 until antKataloger) {
            val kategoriInfo = readLine()!!.split(" ")
            val kategori = Kategori(kategoriInfo[0], kategoriInfo[1], kategoriInfo.slice(2 until kategoriInfo.size))

            oversikt[i.toString()] = kategori
        }
        var bestaar = true
        for (kat in oversikt.values) {
            if (! bestaar) break
            var antallDenneKategorien = 0
            for (kurskode in kat.kurs) {
                if (kurskode in freddiesKurs) {
                    antallDenneKategorien++
                }
            }

            if (antallDenneKategorien < kat.minKrav.toInt()) bestaar = false
        }
        if (bestaar) println("yes") else println("no")

        info = readLine()!!.split(" ")
    }
}

data class Kategori(
    val antallKurs: String,
    val minKrav: String,
    val kurs: List<String>
    )