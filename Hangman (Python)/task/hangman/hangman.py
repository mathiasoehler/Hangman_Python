import random



words = ["python", "java", "swift", "javascript"]
selected_word = random.choice(words)
masked_word = list(len(selected_word) * "-")
input_letter_list = []
attempts = 8
print("H A N G M A N")
print("")
print(''.join(masked_word))
while attempts > 0:
    input_letter = input("Input a letter: ")
    print("")
    letter = input_letter.islower()

    if len(input_letter) != 1:
        print("Please, input a single letter")
    elif letter != True:
        print("Please, enter a lowercase letter from the English alphabet.")
    elif input_letter in input_letter_list:
        print("You've already guessed this letter.")
    else:
        if input_letter not in selected_word:
            print("That letter doesn't appear in the word.")
            attempts -= 1
            input_letter_list.append(input_letter)

        else:
            input_letter_list.append(input_letter)
            for i, letter in enumerate(selected_word):
                if letter == input_letter:
                    masked_word[i] = input_letter
        print(''.join(masked_word))
        if "-" not in masked_word:
            print(f"You guessed the word{selected_word}!")
            print("You survived!")
            attempts = 0
if "-" in masked_word:
    print("")
    print("You lost!")
