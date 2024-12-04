import Data.List

flatten :: [String] -> String
flatten (x:xs) = x ++ "a" ++ flatten xs
flatten [] = ""

diag :: [String] -> [String]
diag grid = dodiag grid (length grid-1) (length (head grid)-1)

dodiag :: [String] -> Int -> Int -> [String]
dodiag grid 0 0 = singleton $ findline grid 0 0
dodiag grid line 0 = findline grid line 0 : dodiag grid (line-1) 0
dodiag grid line col = findline grid line col : dodiag grid line (col-1)


findline :: [String] -> Int -> Int -> String
findline grid 0 col = singleton $ grid!!0!!col
findline grid line col = grid!!line!!col : if col /= (length (head grid)-1) then findline grid (line-1) (col+1) else ""

countxmas :: String -> Int
countxmas ('X':'M':'A':'S':xs) = 1 + countxmas xs
countxmas (_:xs) = countxmas xs
countxmas [] = 0


main::IO()
main = do
    contents <- readFile "input.txt"
    let
        grid = lines contents
        nf = countxmas $ flatten grid
        nr = countxmas $ reverse $ flatten grid
        cf = countxmas $ flatten $ transpose grid
        cr = countxmas $ reverse $ flatten $ transpose grid
        drf = countxmas $ flatten $ diag grid
        drr = countxmas $ reverse $ flatten $ diag grid
        dlf = countxmas $ flatten $ diag $ reverse grid
        dlr = countxmas $ reverse $ flatten $ diag $ reverse grid
        total = nf + nr + cf + cr + drf + drr + dlf + dlr

    print $ total