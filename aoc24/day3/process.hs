import Data.Char
import Text.XHtml (content)

dont :: [Char] -> Int
dont ('d':'o':'(':')':rest) = domul rest
dont (_:rest) = dont rest

domul :: [Char] -> Int
domul ('d':'o':'n':'\'':'t':'(':')':rest) = dont rest
domul ('m':rest) = findmul ('m':rest) + domul rest
domul (_:rest) = domul rest
domul _ = 0


findmul :: [Char] -> Int
findmul ('m':'u':'l':'(':rest) = getnum rest 0 
-- findmul (_:rest) = findmul rest
findmul _ = 0

getnum :: [Char] -> Int -> Int
getnum (c:rest) acc = if isDigit c then getnum rest (acc*10 + digitToInt c) else findcomma (c:rest) acc
getnum [] _ = 0

findcomma :: [Char] -> Int -> Int
findcomma (',':rest) acc = getnum2 rest acc 0
findcomma _ _ = 0

getnum2 :: [Char] -> Int -> Int -> Int
getnum2 (c:rest) acc acc2 = if isDigit c then getnum2 rest acc (acc2*10 + digitToInt c) else findclose (c:rest) acc acc2
getnum2 [] _ _ = 0

findclose :: [Char] -> Int -> Int -> Int
findclose (')':rest) acc acc2 = acc * acc2
findclose _ _ _ = 0


main::IO()
main = do
    contents <- readFile "input.txt"
    let total = domul contents
        
    print total