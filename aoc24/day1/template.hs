addone :: Num a => a -> a
addone a = a +1

mysum :: [Int] -> Int
mysum [] = 0
mysum (x : y) = addone x + mysum y

sumdown :: [[Int]]-> [[Int]] -> [[Int]]
sumdown (current : below : _ ) ((this : line) : column)= 



main::IO()
main = do
    contents <- readFile "input.txt"
    let cases = lines contents
        strnums = [ words x | x <- cases]
        outlist = [0]
        nums = [[read x :: Int| x <- y] | y <- strnums]

    print nums
