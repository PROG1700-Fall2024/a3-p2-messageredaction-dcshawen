"""
    Title: Program 2 - Message Redaction
    Author: Dan Shaw w0190983
    Description: Design and write a program that counts and removes all desired letters from any user-entered sentence or phrase.
"""

import ds_tower1_3_1 as tower

def main():
    title = "Message Redaction Program"
    firstRun = True
    inputString = ""
    
    # Outputs formatted title
    print(tower.Template.titleOut(title))

    while True: 
        if (inputString := getInputString(firstRun)).upper() == "QUIT" or inputString.upper() == "Q":
            break

        lettersToRedact = getLettersToRedact()

        outputString, count = redact(inputString, lettersToRedact)

        print("Redacted message: " + outputString)
        print("Number of letters redacted: " + str(count))
        firstRun = False
    print(tower.Template.getLine("-"))
    print("Thank you for using the Message Redaction Program")
    print("Goodbye.")

def redact(string:str, letters:list):
    """ Iterate through the inputString and keep a count of every character replaced for output later.
     Returns the redacted string and the count of redacted characters. """

    count = 0
    for c in string:
        if c.upper() in letters:
            string = string.replace(c, "_")
            count += 1
    
    return string, count

def getInputString(firstRun:bool):
    """ Gets the input string from the user. On subsequent runs, the instruction will change. """

    if firstRun == True:
        instr = "Enter a sentence or phrase (Quit to exit program): "
    else:
        instr = "Enter another sentence or phrase (Quit to exit program): "
    return input(instr)

def getLettersToRedact():
    """ Gets the letters to redact from the user. """

    print("Enter a comma-separate list of letters to redact")
    while (lettersToRedact := validateCharacterList(input("> ").split(","))) == None:
        print("Invalid input\nEnter a comma-separate list of letters to redact")
    
    return lettersToRedact

def validateCharacterList(list):
    """ Validates whether list is a valid list of characters. Returns a list of characters if successful. Returns None if fails. """
    for i in range(len(list)):
        list[i] = list[i].strip() # Removes whitespace. This allows the user to use spaces in their comma-separated list
        list[i] = list[i].upper()
        if len(list[i]) != 1 or not list[i].isalpha(): # If the resultant string is more than one character, or not a letter, return None
            return None

    return list

if __name__ == "__main__":
    main()