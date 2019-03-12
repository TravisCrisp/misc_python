def ubbi_dubbi(text):
    """"Takes a string and converts it to a form of jibberish.

    Adds a sound like "ub" or "ob" before every vowel syllable."""

    text = text + "  "
    # Allows enumerate(text[:-2]) to loop over all of the input text.

    new_text = ""
    consonants = "bcdfghjklmnpqrstvwxz"
    vowels = "aeiou"
    vowel_combos = ["ae", "ai", "ao", "au", "ea", "ee", "ei", "ie",
                    "io", "oa", "oe", "oi", "oo", "ou", "ue", "ui"]
    # Vowel combinations are stored as list elements to avoid spaces.
    # Exclude the combinations "eo", "ia", "iu", and "ua".

    ub = choose_style()
    # Allows the user to choose jibberish style.

    for i, char in enumerate(text[:-2]):
        while True:
            
            if char.lower() not in vowels \
            and char.lower() != "y":
                new_text += char
            # Adds all spaces and characters other than vowels and "y".     

            elif char.isupper() \
            and char.lower() in vowels:
                new_text += ub.capitalize() + char.lower()
            # Adds all capitalized vowels and converts them to lowercase.
            # Adds "Ub" before the converted vowel.

            elif char == "u" \
            and text[i-1].lower() == "q":
                new_text += char
            # Adds "u" directly following a "q".
            # Dismisses the "u" as a syllable.  

            elif char in vowels \
            and text[i-2].lower() + text[i-1].lower() == "qu":
                new_text += ub + char
            # Adds a vowel directly following a "qu".
            # Adds "ub" before the syllable.

            elif text[i-2].lower() + text[i-1].lower() in vowel_combos:
                new_text += ub + char
            # Adds a vowel that comes after two vowels.
            # Adds "ub" before the syllable.

            elif char == "o" \
            and text[i-1] == "i" \
            and text[i+1].isalpha() == False:
                new_text += ub + char
            # Adds "i" before an "o" at the end of a word.
            # Adds "ub" before the syllable.

            elif char == "i" \
            and text[i-1] == "e" \
            and text[i-2]  == "b":
                new_text += ub + char
            # Adds "i" after "be".
            # Adds "ub" before the syllable.

            elif text[i-1].lower() + char.lower() in vowel_combos:
                new_text += char
            # Adds the second vowel of a vowel combination.
            # Dismisses the vowel as a syllable.

            elif char == "e" \
            and text[i-2].isalpha() == False \
            and text[i-1] not in vowels:
                new_text += ub + char
            # Adds "e" if it's the second letter of a word and the first vowel.
            # Adds "ub" before the syllable.

            elif char == "e" \
            and text[i+1].isalpha() == False \
            and text[i-1].lower() not in "bh":
                new_text += char
            # Adds "e" when it's the last letter of a word and not after "bh".
            # Dismisses the "e" as a syllable (silent).

            elif char == "e" \
            and text[i+1] == "s" \
            and text[i-1] not in "bgh":
                new_text += char    	    
            # Adds "e" when it comes before "s" and not after "bgh".
            # Dismisses the "e" as a syllable (silent).

            elif char == "e" \
            and text[i+1] == "d" \
            and text[i-1] in "cgkpswz":
                new_text += char
            # Adds "e" when it comes before "d" and after "cgkpswz"
            # Dismisses the "e" as a syllable (silent).

            elif char in vowels:
                new_text += ub + char
            # Adds any remaining vowels.
            # Adds "ub" before the syllable.

            elif char == "y" \
            and text[i-1].lower() in consonants \
            and text[i+1].lower() + text[i+2].lower() in vowel_combos:
                new_text += ub + char
            # Adds "y" when preceeding two vowels.
            # Adds "ub" before the syllable.

            elif char == "y" \
            and text[i-1].lower() in consonants \
            and text[i+1].lower()not in "aeou":
                new_text += ub + char
            # Adds "y" when not followed by "aeou".
            # Adds "ub" before the consonant.

            elif char.lower() == "y" \
            and text[i-1].lower() in consonants \
            and text[i+1].lower() not in vowels:
                new_text += ub.capitalize() + char.lower()
            # Adds capital "y" and converts to lower case.
            # Adds "ub" before the "y".

            else:
                new_text += char
            # Adds any remaining "y".

            break

    print(f"\n{new_text}\n")

    again = do_again()
    if again == "y":
        text = input("\nEnter Your Text: ")
        ubbi_dubbi(text)
    else:
        print(f"\nG{ub}oodb{ub}ye!\n")

def choose_style():
    """Asks the user to choose a jibberish style for the text.

    Continues until a proper input is recieved."""
    
    while True:
        ub = input("\nConvert to Ubbi Dubbi (ub), Obbi Dobbi (ob), or Ibbi Dibbi, (ib)? ")
        if ub.lower() in ["ub", "ob", "ib"]:
            return ub.lower()
        print("\nI Don't Understand!")

def do_again():
    """Asks user if they would like to perform ubbi_dubbi() again.

    Continues until a proper input is recieved."""

    while True:
        answer = (input("Convert More Text? Yes (y), No (n): "))
        if answer.lower() in "yn":
            return answer.lower()
        print("\nI Don't Understand!\n")

if __name__ == '__main__':
    text = input("\nEnter Your Text: ")
    ubbi_dubbi(text)  