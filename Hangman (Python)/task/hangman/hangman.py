# Write your code here
def teaser():
    print("""H A N G M A N
    The game will be available soon.""")


def play(words_list):
    guest = str(input("Guess the word:")).lower()
    if guest in words_list:
        print("You survived!")
    else:
        print("You lost!")


words = ["python"]
play(words)
