import Foundation

func main() {

    guard let forbiddenChars = readLine() else { return }
    guard let msg = readLine() else { return }

    var result = ""

    let msgArray = msg.components(separatedBy: " ")

    for word in msgArray {
        var hasBeenBlurred = false
        for char in forbiddenChars {
            if hasBeenBlurred {continue}
            
            if word.contains(char) {
                result += String(repeating: "*", count: word.count)
                hasBeenBlurred = true
            } 
        }
        if !hasBeenBlurred {
            result += word
        }
        result += " "
    }
    print(result)
}

main()