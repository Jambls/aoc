import Data.List


extract_rules ("":xs) = []
extract_rules (x:xs) = x: extract_rules xs

extract_pages ("":xs) = xs
extract_pages (x:xs) = extract_pages xs

main::IO()
main = do
    contents <- Prelude.readFile "inputsmall.txt"
    let
        grid = lines contents
        rules = sort $ extract_rules grid
        pages = extract_pages grid


    print rules