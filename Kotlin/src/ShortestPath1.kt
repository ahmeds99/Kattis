import java.util.*
import kotlin.Comparator
import kotlin.collections.HashMap
import kotlin.collections.HashSet

fun main() {
    val tast = Scanner(System.`in`)
    var linje = tast.nextLine()

    while (linje != "0 0 0 0") {
        val info = linje.split(" ").map {it.toInt()}
        val noder = info[0]; val kanter = info[1]; val q = info[2]; val s = info[3].toString()
        val graf = HashMap<String, HashSet<Node>>()

        for (i in 0 until noder) graf[i.toString()] = HashSet()

        for (i in 0 until kanter) {
            val kant = tast.nextLine().split(" ")
            graf[kant[0]]?.add(Node(kant[1], kant[2].toInt()))
        }

        val shortestPaths = Dijkstra(graf, s)
        for (i in 0 until q) {
            val slutt = tast.nextLine()
            when (shortestPaths[slutt]) {
                Int.MAX_VALUE -> println("Impossible")
                else -> println(shortestPaths[slutt])
            }
        }
        linje = tast.nextLine()
        println()
    }
}

/*
Tar inn en graf, og startpunktet. Kan optimaliseres ved å returnere når vi popper sluttdestinasjonen
fra prioritetskøen, men jeg trenger vektene til alle ettersom det forekommer flere 'queries', og jeg
ikke ønsker å kjøre Dijkstra for hver query.
 */
fun Dijkstra(graf: HashMap<String, HashSet<Node>>, start: String): HashMap<String, Int> {
    val D = HashMap<String, Int>()
    val Q = PriorityQueue(ComparatorNode())

    for ((node, _) in graf) D[node] = Int.MAX_VALUE
    D[start] = 0
    Q.add(Node(start, 0))

    while (! Q.isEmpty()) {
        val node = Q.poll()
        //if ((node.name) == slutt) return D

        for (nabo in graf[node.name]!!) {
            val cost = D[node.name]?.plus(nabo.cost)
            if (cost != null) {
                if (cost < D[nabo.name]!!) {
                    D[nabo.name] = cost
                    Q.add(Node(nabo.name, cost))
                }
            }
        }
    }
    return D
}

// Meget digg funksjonalitet ved Kotlin
data class Node(val name: String, val cost: Int)

class ComparatorNode : Comparator<Node> {
    override fun compare(o1: Node?, o2: Node?): Int {
        return if (o1 == null || o2 == null) 0 else o1.cost.compareTo(o2.cost)
    }
}