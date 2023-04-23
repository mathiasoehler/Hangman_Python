# Write your code here
def teaser():
    print("H A N G M A N")


def play(words_list):
    from random import choice
    searching_word = choice(words_list)
    guest = str(input("Guess the word:")).lower()
    if guest in searching_word:
        print("You survived!")
    else:
        print("You lost!")


words = ["python", "java", "swift", "javascript"]

teaser()
play(words)
