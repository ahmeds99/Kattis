import java.util.Scanner
import java.util.ArrayDeque

fun main() {
    val tast = Scanner(System.`in`)
    val antCaser = tast.nextLine().toInt()

    for (i in 0 until antCaser) {
        val info = tast.nextLine()
        val stack = ArrayDeque<Char>()
        var skrevetUt = false

        for (c in info) {
            if (c == '$' || c == '|' || c == '*') stack.push(c)
            else if (c == 'b') {
                if (stack.peek() == '$') stack.pop()
                else {
                   skrevetUt = true; break
                }
            } else if (c == 't') {
                if (stack.peek() == '|') stack.pop()
                else {
                    skrevetUt = true; break
                }
            } else if (c == 'j') {
                if (stack.peek() == '*') stack.pop()
                else {
                    skrevetUt = true; break
                }
            }
        }
        if (stack.isEmpty() && !skrevetUt) println("YES") else println("NO")
    }
}