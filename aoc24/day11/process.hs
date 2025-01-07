
split myList = pairToList$ splitAt ((length myList + 1) `div` 2) myList

pairToList (x,y) = [x,y]



step :: [Int] -> [Int]
step [] = []
step (0:xs) = 1 : step xs
step (x:xs) = if even (Prelude.length $ show x) then [read y :: Int | y <- split $ show x] ++ step xs else x*2024 : step xs

go 0 lst = lst
go x lst = go (x - 1) $ step lst

main::IO()
main = do
    contents <- Prelude.readFile "input.txt"
    let
        start = [read x :: Int | x <- Prelude.words contents]


    print $ length $ go 45 start