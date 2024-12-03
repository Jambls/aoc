import Data.List

-- this doesn't work

checkupunsafefirst (x : y : list)
  | x +1 <= y && x +3 >= y = checkupunsafe (y:list)
  | (checkup (x:list) + checkup (y:list)) > 0 = 1
  | otherwise = 0
checkupunsafefirst [_] = 1

checkupunsafe (x : y : z : list)
  | (x +1 <= y && x +3 >= y) && (y+1 <= z && y +3 >= z) = checkupunsafe (y:z:list)
  | x+1 <= z && x +3 >= z = checkup (x:z:list)
  | x +1 <= y && x +3 >= y = checkupunsafe (y:z:list)
  | otherwise = 0
checkupunsafe (x:y:list) = if x +1 <= y && x +3 >= y then checkupunsafe(y:list) else checkup (x:list)
checkupunsafe [_] = 1

checkup (x:y:list) = if x +1 <= y && x +3 >= y then checkup (y:list) else 0
checkup [_] = 1



checkdownunsafefirst (x : y : list)
  | x -1 >= y && x -3 <= y = checkdownunsafe (y:list)
  | (checkdown (x:list) + checkdown (y:list)) > 0 = 1
  | otherwise = 0
checkdownunsafefirst [_] = 1

checkdownunsafe (x:y:list) = if x -1 >= y && x -3 <= y then checkdownunsafe (y:list) else checkdown (x:list)
checkdownunsafe [_] = 1


checkdown (x:y:list) = if x -1 >= y && x -3 <= y then checkdown (y:list) else 0
checkdown [_] = 1

check lst = if  checkdownunsafefirst lst + checkupunsafefirst lst > 0 then 1 else 0

main::IO()
main = do
    contents <- readFile "input.txt"
    let cases = lines contents
        strnums = [ words x | x <- cases]
        nums = [[read x :: Int| x <- y] | y <- strnums]
        checked = [check x | x<- nums]
        total = sum checked
    print checked