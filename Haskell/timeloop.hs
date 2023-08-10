solve :: Int -> [String]
solve n = zipWith (curry tupleToString) [1..n] (replicate n "Abracadabra")

tupleToString :: (Int, String) -> String
tupleToString (i, s) = show i ++ " " ++ s

main = interact (unlines . solve . read)