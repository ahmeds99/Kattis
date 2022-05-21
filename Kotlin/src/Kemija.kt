fun main() {
    val word = readLine()!!
    var originalWord = ""
    var i = 0

    while (i < word.length) {
        originalWord += word[i]
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')
            i += 2
        i++
    }
    println(originalWord)
}