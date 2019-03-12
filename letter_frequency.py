def letter_frequency(text):
    """ Returns the frequency of each letter in input text. 

    Allows the user to choose a sorting method."""

    d = {}
    for char in text.lower():
        if char.isalpha():
            d[char] = d.get(char, 0) + 1
            # Creates a dictionary of letters and their occurence.

    d_pairs = sorted(d.items())
    # Creates a list of tuple pairs from the dictionary.

    sort = choose_sort()
    if sort == "l":
        d_pairs.sort(key=lambda v: v[-1])
    if sort == "g":
        d_pairs.sort(key=lambda v: v[-1], reverse=True)
        # Allows the user to choose a sorting method.

    for k, v in d_pairs:
        print(f"\n\"{k}\" occurence: {v}")

    again = do_again()
    if again == "y":
        text = input("\nEnter Your Text: ")
        letter_frequency(text)
    else:
        print("\nGoodbye!\n")
            
def choose_sort():
    """ Asks the user to choose a sorting method.

    Continues until a proper input is recieved."""

    while True:
        sort = input("\nSort Alphabetically (a) or by Frequency (f)? ")
        if sort.lower() in "a":
            return sort.lower()
        elif sort.lower() in "f":
            while True:
                sort = input("\nSort by Least (l) or Greatest (g) Occurence? ")
                if sort.lower() in "lg":
                    return sort.lower()
                print("\nI Don't Understand!")
        print("\nI Don't Understand!")
            
def do_again():
    """ Asks the user if they would like to use the function again.

    Continues until a proper input is recieved."""

    while True:
        again = input("\nEnter More Text? Yes (y) or No (n): ")
        if again.lower() in "yn":
            return again.lower()
        print("\nI Don't Understand!")    

if __name__ == '__main__':
    text = input("\nEnter Your Text: ")
    letter_frequency(text)