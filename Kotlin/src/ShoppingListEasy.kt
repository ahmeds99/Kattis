
fun main() {
    val info = readLine()!!.split(" ")
    val lister = info[0].toInt()
    val felles = HashMap<String, Int>()

    for (i in 0 until lister) {
        val liste = readLine()!!.split(" ")
        for (vare in liste) {
            felles[vare] = felles.getOrDefault(vare, 0) + 1
        }
    }

    val resultat = ArrayList<String>()
    for ((vare, antall) in felles) {
        if (antall == lister) { // da er varen med i alle lister
            val indeks = -(resultat.binarySearch(vare) + 1)
            resultat.add(indeks, vare)
        }
    }
    println(resultat.size)
    for (vare in resultat) println(vare)
}