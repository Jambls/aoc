import Data.List

addone :: Num a => a -> a
addone a = a +1

mysum :: [Int] -> Int
mysum [] = 0
mysum (x : y) = addone x + mysum y

distance a b = abs (a - b)




main::IO()
main = do
    contents <- readFile "input.txt"
    let cases = lines contents
        strnums = [ words x | x <- cases]
        nums = [[read x :: Int| x <- y] | y <- strnums]
        transformed = unzip[ (a,b)| (a:b:_) <- nums]
        (left, right) = transformed
        sleft = sort left
        sright = sort right
        sorted = zip sleft sright
        distances = [distance a b | (a,b) <- sorted]
        total = sum distances


    print total
