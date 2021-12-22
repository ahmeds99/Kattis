fun main() {
    val setning = readLine()?.split(" ")
    var antDialekt = 0

    if (setning != null) {
        for (ord in setning) {
            if ("ae" in ord) antDialekt += 1
        }
        val andel = antDialekt * 100 / setning.size
        if (andel >= 40) println("dae ae ju traeligt va") else println("haer talar vi rikssvenska")
    }
}