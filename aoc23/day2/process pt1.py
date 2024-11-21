import re


valid_gmes = 0

with open("input.txt", "r") as f:
    for line in f:
        colon_index = line.find(":")
        gameID = line [4:colon_index]
        colours = re.split(";|,", line[colon_index + 2 :].strip())
        red = 0
        green = 0
        blue = 0
        for elt in colours:
            elt = elt.strip()
            space_index = elt.find(" ")
            if elt[space_index+1:space_index+2] == "r":
                temp = int(elt[:space_index])
                if temp > red:
                    red = temp
            elif elt[space_index+1:space_index+2] == "g":
                temp = int(elt[:space_index])
                if temp > green:
                    green = temp
            elif elt[space_index+1:space_index+2] == "b":
                temp = int(elt[:space_index])
                if temp > blue:
                    blue = temp
            else:
                print(space_index)
                raise Exception(elt[space_index+1:space_index+2] + "not r g or b")
            #print(elt)
        
        #print(red , " " , green , " " , blue , " " , gameID)
        if red < 13 and green < 14 and blue < 15:
            
            valid_gmes += int(gameID)

print(valid_gmes)