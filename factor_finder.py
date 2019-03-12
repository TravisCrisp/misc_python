def factor_finder(num):
    """Finds all the factors of input number.

    Sorts factors by whether they are composite or prime."""

    factors = [n for n in range(2, int(num/2) + 1) if num%n == 0]
    composite = []
    
    for i, v in enumerate(factors):
        for n in factors[:i]:
            if v%n == 0 and v not in composite:
                composite.append(v)
                # Builds a unique list of composite factors.
    
    prime = [n for n in factors if n not in composite]
    # Builds a prime list by comparing factors and composite factors.

    composite = [str(n) for n in composite]
    if composite == []:
        composite = ["None"]
    prime = [str(n) for n in prime]
    # Converts lists to contain strings instead of integers.
    if len(factors) == 0:
        print(f"\n{num} is Prime!\n")
    else:
        print(f"\nFactors of {num}")
        print("\nComposite: {}".format(", ".join(composite)))
        print("\nPrime: {}\n".format(", ".join(prime)))
    
    again = do_again()
    if again == "y":
        n = get_num()
        factor_finder(n)
    else:
        print("\nGoodbye!\n")   

def get_num():
    """ Asks user for a number.

    Continues until a proper input is recieved."""

    while True:
        num = input("\nEnter a Number to Find its Factors: ")
        if num.isdigit():
            return int(num)
        print("\nThat's Not a Number!")

def do_again():
    """Asks user if they would like to factor another number.

    Continues until a proper input is recieved."""
    
    while True:
        answer = (input("Factor Another Number? Yes (y), No (n): "))
        if answer.lower() in "yn":
            return answer.lower()
        print("\nI Don't Understand!\n")     

if __name__ == '__main__':
    n = get_num() 
    factor_finder(n)