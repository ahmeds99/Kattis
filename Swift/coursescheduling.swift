import Foundation

func main() {
    let numInputs = Int(readLine()!)!
    var courseInfo: [String : Set<String>] = [:]

    for _ in 0..<numInputs {
        let info = readLine()!.components(separatedBy: " ")
        let (firstName, lastName, course) = (info[0], info[1], info[2])
        let fullName = firstName + " " + lastName

        courseInfo[course, default: []].insert(fullName)
    }

    for (course, students) in courseInfo.sorted(by: { $0.key < $1.key }) {
        print(course, students.count)
    }

}

main()