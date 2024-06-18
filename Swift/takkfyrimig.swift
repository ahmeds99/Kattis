
func main () {
    guard let numOfGuests = readLine() else { return }
    guard let guestToInt = Int(numOfGuests) else { return }

    for _ in 0..<guestToInt {
        let name = readLine()
        print("Takk " + (name ?? ""))
    }
}
main()