import Data.List

distance a b = abs (a - b)

occurances target (check:list) = (if target == check then 1 else 0) + occurances target list
occurances _ [] = 0

harvest (a:alist) (b:blist) = a * b + harvest alist blist
harvest [] [] = 0


main::IO()
main = do
    contents <- readFile "input.txt"
    let cases = lines contents
        strnums = [ words x | x <- cases]
        nums = [[read x :: Int| x <- y] | y <- strnums]
        transformed = unzip[ (a,b)| (a:b:_) <- nums]
        (left, right) = transformed
        similarities = [occurances a right | a <- left]

        total = harvest left similarities


    print total
