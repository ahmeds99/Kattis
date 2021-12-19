import java.util.Scanner
/*
Actually, this problem is a lot simpler than first imagined,
you dont even need a DFS.
 */
fun main() {
    val tast = Scanner(System.`in`)

    val antallCaser = tast.nextLine().toInt()

    for (i in 1..antallCaser) {
        val graf = HashMap<String, ArrayList<String>>()
        val besokteNoder = HashSet<String>()
        val info = tast.nextLine().split(" ")
        val antNoder = info[0].toInt(); val antKanter = info[1].toInt()

        for (j in 1..antKanter) {
            val kant = tast.nextLine().split(" ")

            if (! graf.containsKey(kant[0]))
                graf[kant[0]] = ArrayList()

            if (! graf.containsKey(kant[1]))
                graf[kant[1]] = ArrayList()

            graf[kant[0]]?.add(kant[1])
            graf[kant[1]]?.add(kant[0])
        }
        val start = graf.keys.first()
        println(antNoder - 1)
        //println(DFS(start, graf, 0, besokteNoder))
    }
}

fun DFS(node: String, graf: HashMap <String, ArrayList<String>>,
        antall: Int, besokteNoder: HashSet<String>): Int {

    besokteNoder.add(node)
    var antallet = antall

    for (nabo in graf[node]!!) {
        if (besokteNoder.contains(nabo)) continue
        return DFS(nabo, graf, ++antallet, besokteNoder)
    }
    return antallet
}