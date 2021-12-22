
fun main() {
    var linje = readLine()

    while (linje != "0 0 0 0") {
        val info = linje!!.split(" ").map { it.toInt() }
        val noder = info[0]; val kanter = info[1]; val q = info[2]; val s = info[3].toString()
        val graf = HashMap<String, HashSet<Node>>()

        for (i in 0 until noder) graf[i.toString()] = HashSet()

        for (i in 0 until kanter) {
            val kant = readLine()!!.split(" ")
            graf[kant[0]]?.add(Node(kant[1], kant[2].toInt()))
        }

        val shortestPaths = BellmanFord(graf, s)
        for (i in 0 until q) {
            val slutt = readLine()
            when (shortestPaths[slutt]) {
                Int.MAX_VALUE -> println("Impossible")
                Int.MIN_VALUE -> println("-Infinity")
                else -> println(shortestPaths[slutt])
            }
        }
        linje = readLine()
        println()
    }
}

fun BellmanFord(graf: HashMap<String, HashSet<Node>>, start: String): HashMap<String, Int> {
    val D = HashMap<String, Int>()

    for ((node, _) in graf) D[node] = Int.MAX_VALUE
    D[start] = 0

    for (i in 0 until graf.size) {
        for ((node, naboer) in graf) {
            for (nabo in naboer) {
                val cost = D[node]!! + nabo.cost
                if (cost < D[nabo.name]!!) D[nabo.name] = cost
            }
        }
    }

    for ((node, naboer) in graf) {
        for (nabo in naboer) {
            val cost = D[node]!! + nabo.cost
            // negativ sykel hvis kondisjonen slår inn
            if (D[nabo.name] != Int.MAX_VALUE && cost < D[nabo.name]!!) D[nabo.name] = Int.MIN_VALUE
        }
    }
    return D
}
