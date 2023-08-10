solve :: [Int] -> Int
solve (a:b:rest) = if a > b then 1 else 0

readInput = map read . words

main = interact (show . solve . readInput)