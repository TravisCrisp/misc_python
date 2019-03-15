import itertools
import enchant

d = enchant.Dict("en_US")

def get_words(word):
    """Returns all possible words of three of more letters
    that can be made with the letters of the input word."""
    
    word_list = []
    for i, letter in enumerate(word):
        letter_combos = itertools.permutations(word, i+3)
        for letters in letter_combos:
            word_list.append("".join(letters))
    
    word_list = set(word_list)
    word_list.remove(word)
    
    is_word = [w for w in word_list if d.check(w)]
    is_word.sort()
    is_word.sort(key=len)

    if is_word == []:
        print(f"\nNo other words possible from \"{word}\".")
    else:
        print(f"\nPossible words from \"{word}\":\n")
        for w in is_word:
            print(w)
    
    answer = do_again()
    if answer == "y":
        word = get_word()
        get_words(word)
    else:
        print("\nGoodbye!\n")
    
def get_word():
    while True:
        word = input("\nEnter a Word: ")
        if word.isalpha():
            return word.lower()
        elif " " in word:
            print("\nNo Spaces Please!")
            continue
        elif len(word) < 3:
            print("\nMust be Three or More Letters!")
            continue
        print("\nOnly Letters Please!")

def do_again():
    while True:
        answer = input("\nContinue? Yes (y), No (n): ")
        if answer.lower() in "yn":
            return answer
        print("\nI Don't Understand!")
           
if __name__=='__main__':
    word = get_word()
    get_words(word)