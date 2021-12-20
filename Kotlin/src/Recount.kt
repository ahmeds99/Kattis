import java.util.Scanner

fun main() {
    val tast = Scanner(System.`in`)
    val oversikt = HashMap<String, Int>()
    var flestStemmer = 0; var harFlest = ""
    var toLike = false

    var linje = tast.nextLine()
    while (linje != "***") {
        when (val antall = oversikt[linje]) {
            null -> oversikt[linje] = 1
            else -> oversikt[linje] = antall + 1
        }
        // using the double bang-operator because oversikt[linje] is never null
        if (oversikt[linje]!! > flestStemmer) {
            flestStemmer = oversikt[linje]!!
            harFlest = linje; toLike = false
        } else if (oversikt[linje]!! == flestStemmer) {
            toLike = true
        }
        linje = tast.nextLine()
    }
    if (! toLike) println(harFlest) else println("Runoff!")
}
