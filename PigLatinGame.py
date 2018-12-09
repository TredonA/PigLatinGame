# Pig Latin Game program | By Tredon Austin

def firstVowel(word):
    index = 0
    while index != len(word):
        if word[index] in 'aeiou':
            return index
        else:
            index += 1
    return index

def pigLatinConverter():
    userWord = input("Welcome to my Pig Latin converter! " +\
       "Please enter a word: ")
    if not userWord.isalpha():
        print("Word contains a space or invalid character! Ending program...")
        return
    vowelPos = firstVowel(userWord)
    if vowelPos == len(userWord):
        print("Word does not contain a traditional vowel! Ending program...")
        return
    elif vowelPos == 0:
        print("Before Pig Latin:\t" + userWord)
        print("After Pig Latin:\t" + userWord + "way")
    else:
        firstHalf = userWord[vowelPos:]
        secondHalf = userWord[:vowelPos] + 'ay'
        print("Before Pig Latin:\t" + userWord)
        print("After Pig Latin:\t" + firstHalf + secondHalf)
    resetCMD = input("Would you like to use the program again? " +\
        "Press 1 if Yes or 2 if No: ")
    if resetCMD == '1':
        pigLatinConverter()
    elif resetCMD == '2':
        print("Thank you for using my program! Ending now...")
        return
    else: 
        print("Unrecognized command! Ending now...")
        return
    return

pigLatinConverter()