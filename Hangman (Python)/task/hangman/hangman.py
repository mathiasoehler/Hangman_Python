import random

print("H A N G M A N")
word = random.choice(['python', 'java', 'swift', 'javascript'])
letters = dict({c: '-' for c in word})
word_game = ("\n" + "".join(letters[c] for c in word)) # gibt das Wort mit - aus
counter = 0 # runden Zähler
word_set = set(word)
kontrolle = set() # alle buchstaben vom Wort enthalten

while counter < 8:
    print(len(kontrolle))
    print(len(word_set))
    print(kontrolle)
    print(word_set)

    counter += 1
    word_game = ("\n" + "".join(letters[c] for c in word)) # gibt das Wort mit - aus
    print(word_game)
    new_letter = input("Input a letter:")
    if new_letter in letters: # wenn der gültige Buchstabe eingegeben wird wird dieser aufgedeckt
        letters[new_letter] = new_letter
        kontrolle.add(new_letter)
        print("new")
    elif new_letter not in letters:  # Ausgabe wenn der Buchstabe nicht im Wort enthalten ist: "That letter doesn't appear in the word"
        print("That letter doesn't appear in the word")

    elif new_letter in kontrolle:# bei einer doppeleingabe des Buchstaben: No improvements.
        print("No improvements.")
    elif len(kontrolle) == len(word_set):  # Wenn der Spieler gewinnt ausgabe von: Siehe bsp.
        print("test")

print("\nThanks for playing!")