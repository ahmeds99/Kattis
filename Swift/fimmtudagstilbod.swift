func main() {
    guard let year = Int(readLine()!) else { return }
    let price = year <= 2020 ? 1000 : 1000 + (100 * (year - 2020))
    print(price)
}

main()