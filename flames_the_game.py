def names_letterSorter (firstName, secondName):
    lettersCancelled = 0
    for i in firstName:
        for j in secondName:
            if i == j:
                lettersCancelled += 1
                break
    letters_inFirstName = len(firstName) - lettersCancelled
    letters_inSecondName = len(secondName) - lettersCancelled
    return letters_inFirstName + letters_inSecondName

def remainingLetters_interpreter (remainingLetters):
    if remainingLetters % 6 == 0:
        return "\t You can do better, infatuation isn\'t love"
    elif remainingLetters % 6 == 1:
        return "\t Oops! You guys are friends."
    elif remainingLetters % 6 == 2:
        return "\t Ooh... love birds!"
    elif remainingLetters % 6 == 3:
        return "\t Admiriers can also ignite a flame."
    elif remainingLetters % 6 == 4:
        return "\t Who knows, maybe you are raw materails for marriage."
    elif remainingLetters % 6 == 5:
        return "\t How long do you plan to be enemies though?"

userChoice = True

while userChoice:
    first_name = list (input("Enter guy\'s name: "))
    second_name = list (input("Enter girl\'s name: "))

    remainingLetters = names_letterSorter (first_name, second_name)

    print (remainingLetters_interpreter (remainingLetters))

    userChoice = str (input("Would you like to continue (yes/no): "))

    if (userChoice == "yes"):
       userChoice = True
    else:
       userChoice = False 
