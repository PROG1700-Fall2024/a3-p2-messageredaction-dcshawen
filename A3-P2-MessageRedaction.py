"""
    Title: Program 2 - Message Redaction
    Author: Dan Shaw w0190983
    Description: Design and write a program that counts and removes all desired letters from any user-entered sentence or phrase.
"""

from webbrowser import get
import ds_tower1_3_0 as tower

def main():
    title = "Message Redaction Program"
    print(tower.Template.titleOut(title))

    inputString = ""

    while True:
        if (inputString := getInputString().upper()) == "QUIT":
            break

        lettersToRedact = getLettersToRedact()

        for c in lettersToRedact:
            inputString = inputString.upper().replace(c.upper(), "_")

        print("Number of letters redacted: " + str(len(lettersToRedact)))
        print("Redacted message: " + inputString)
    
    print("Thank you for using the Message Redaction Program")
    print("Goodbye.")

def getInputString():
    return input("Enter a sentence or phrase (Quit to exit program): ")

def getLettersToRedact():
    print("Enter a comma-separate list of letters to redact")
    while (lettersToRedact := validateCharacterList(input("> ").split(","))) == None:
        print("Invalid input")
    
    return lettersToRedact

def validateCharacterList(list):
    """ Validates whether list is a valid list of characters. Returns a list of characters if successful. Returns None if fails. """
    for c in range(len(list)):
        list[c] = list[c].strip()
        if len(list[c]) != 1:
            return None

    return list

if __name__ == "__main__":
    main()