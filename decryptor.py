global alph
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
puct = [",", ".", ";", ":", "'", "\""]

wordsFile = open("words_alpha.txt", "r")
wordsContent = wordsFile.read()
wordsList = wordsContent.split("\n")
wordsFile.close()

print(len(wordsList))

def getUserInput(sel):
    if sel == 0:
        print("What is the shift: ")
        shift = input()
        print("enter cypher: ")
        cypher = input()
        message = decypher(shift, cypher, 0)
        print(message)
    elif sel == 1:
        print("Message to be decyphered: ")
        cypher = input()
        autodecrypt(cypher)
    elif sel == 2:
        print("What is the shift: ")
        shift = input()
        print("enter cypher: ")
        cypher = input()
        message = decypher(shift, cypher, 1)
        print(message)


def crossCheck(list1, element):
    x = 0
    for i in list1:
        x += 1
        if i == element:
            return x
    
            

def decypher(sh, cy, mode):

    newList = []
    newStr = "\n"
    if mode == 0:
        op = "-"
    elif mode == 1:
        op = "+"

    for i in cy:
        lowerCaseLetter = i.lower()
        if lowerCaseLetter not in alph:
            newList.append(i)
        else:
            initialnum = crossCheck(alph, lowerCaseLetter)
            newNum = eval(str(initialnum) + op + sh)
            if int(newNum) > 26:
                wrappedNum = newNum - 26
                newLetter = alph[wrappedNum - 1]
                newList.append(newLetter)
            else:
                newLetter = alph[newNum - 1]
                newList.append(newLetter)
    for i in newList:
        newStr += str(i)

    return newStr

def autodecrypt(cy):
    matchList = []
    for i in range(0, 26):
        listStr = []
        finStr = "\n"
        initDecypher = decypher(str(i), cy, 0)
        for i in initDecypher:
            lowerCaseLetter = i.lower()
            if lowerCaseLetter in puct:
                continue
            else:
                listStr.append(lowerCaseLetter)
            
        for i in listStr:
            finStr += str(i)
        words = finStr.split()
        x = 0
        
        for i in words:
            if i in wordsList:
                x += 1
            else:
                continue
        matchList.append(x)
    shiftNum = max(matchList)
    shift = matchList.index(shiftNum)
    print(shift)
    message = decypher(str(shift), cy, 0)
    print(message)

    

print("What would you like to do: \ndecrypt: 0\nauto-decrypt: 1\nEncrypt: 2")
userInput = input()
getUserInput(int(userInput))

