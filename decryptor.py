global alph
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
puct = [",", ".", ";", ":", "'", "\""]

def crossCheck(list1, element):
    x = 0
    for i in list1:
        x += 1
        if i == element:
            return x
            

def decypher(sh, cy):
    newList = []
    newStr = "\n"
    for i in cy:
        lowerCaseLetter = i.lower()
        if lowerCaseLetter not in alph:
            newList.append(i)
        else:
            initialnum = crossCheck(alph, lowerCaseLetter)
            newNum = initialnum - int(sh)
            if int(newNum) > 26:
                wrappedNum = newNum - 26
                newLetter = alph[wrappedNum - 1]
                newList.append(newLetter)
            else:
                newLetter = alph[newNum - 1]
                newList.append(newLetter)
    for i in newList:
        newStr += str(i)

    print(newStr)


print("What is the shift: ")
shift = input()
print("enter cypher: ")
cypher = input()

decypher(shift, cypher)