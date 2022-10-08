import pprint
import random
import string
import sys

pp = pprint.PrettyPrinter(indent=2)

letters = {}
evens = {}
odds = {}

def populateLetterDicts():
    global letters
    letters = {ch: n+1 for n, ch in enumerate(string.ascii_lowercase)}
    for letter in letters:
        if letters[letter] % 2 == 0:
            evens[letter] = letters[letter]
        else:
            odds[letter] = letters[letter]

def pickRandomTuple():
    availableLetters = list(letters.keys())
    return [random.choice(availableLetters), random.choice(availableLetters)]

def pickRandomTriple(even):
    t = pickRandomTuple()
    sum = letters[t[0]] + letters[t[1]]
    nextSet = None
    if sum % 2 == 0:
        nextSet = evens if even else odds
    else:
        nextSet = odds if even else evens
    t.append(random.choice(list(nextSet.keys())))
    return t

def removeLetter(letter):
    value = letters[letter]
    if value % 2 == 0:
        if len(evens) == 1:
            print('ERROR: This is your last even letter. Removing it means you cannot generate a coordinate whose sum is even.')
            return
        del evens[letter]
    else:
        if len(odds) == 1:
            print('ERROR: This is your last odd letter. Removing it means you cannot generate a coordinate whose sum is odd.')
            return
        del odds[letter]
    del letters[letter]

def generateAction():
    coordinates = []
    evenIndex = random.randint(0, 5)
    for i in range(6):
        even = (i == evenIndex)
        coordinates.append(pickRandomTriple(even))
    print('The generated coordinates are:')
    for c in coordinates:
        sum = letters[c[0]] + letters[c[1]] + letters[c[2]]
        evenFlag = " <" if sum % 2 == 0 else ""
        print("  " + str(c) + ' => sum is ' + str(sum) + evenFlag)

def removeAction():
    print('The current pool of letters is:')
    pp.pprint(letters)

    choice = 'FOO'
    while (choice not in letters and choice != 'cancel'):
        choice = input('Choose a letter to remove, or type "cancel":\n')
    if choice != 'cancel':
        removeLetter(choice)
    return

def quitAction():
    print('quitting')
    sys.exit()

def main():
    populateLetterDicts()

    # this will loop until you quit
    while(True):
        nextAction = 'FOO'
        validActions = {'g': generateAction, 'r': removeAction, 'q': quitAction}
        while (nextAction not in validActions):
            nextAction = input('Next action: (g)enerate (r)emove (q)uit:\n')
        validActions[nextAction]()
        # extra newline :)
        print()

if __name__ == '__main__':
    main()