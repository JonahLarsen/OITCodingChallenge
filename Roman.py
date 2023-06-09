import argparse

def main (input):

    # If input is a roman numeral
    if isinstance(input, str):
        output = 0  # Initalize output variable, which stores the translated text.
        Roman_Dict = { #Dictionary to easily allow changing from roman numeral to decimal
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        #Loop starts at the second character in the input string 
        #and as it iterates it is keeping track of the current value and the value before it
        previous = Roman_Dict[input[0]]
        current = 0
        i = 1 # counter
        while i < len(input):
            current = Roman_Dict[input[i]]
            if previous < current: # In this case, previous and current make up a subtractive notation number
                output += current - previous
                if i < len(input) - 1:
                    previous = Roman_Dict[input[i+1]]
                i += 2 # Because both previous and current are used to calculate this number, we have to iterate an extra step 
                       # on both previous and current
            else:
                if i == len(input) - 1: # If it's the end of the string, we just add both previous and current without iterating
                    output += previous + current
                else:
                    output += previous # This is the normal case for a non subtractice notation number, just adds previous and then iterates
                    previous = current
                i += 1
        print(output)

    #If input is a decimal
    elif isinstance(input, int):
        output = "" # Initialize a string that will hold the Roman Numerals
        Decimal_Dict = { # Dictionary to store the sets of Roman numerals for each place
            100: ["CM", "D", "C"],
            10: ["XC", "L", "X"],
            1: ["IX", "V", "I"]

        }

        num_thousands = input // 1000  # Because none of the numbers will go into the 10,000s, the 1000s can be taken care of before
        for _ in range(num_thousands): # iterating through the other places
            output += "M"
            input -= 1000

        place = 100
        while input != 0:
            num_places = input // place
            if num_places == 9: # If the number of the place is nine, then the substractive notation should be used
                output += Decimal_Dict[place][0]
                input -= 9 * place
            else:
                if num_places >= 5: # If the number of the place is between 5 and 9, the first 5 are represented by their own symbol
                    output += Decimal_Dict[place][1]
                    num_places -= 5
                    input -= 5 * place
                for _ in range(num_places): # Add all the singular amounts of each place
                    output += Decimal_Dict[place][2]
                    input -= 1 * place
            place = place // 10
        print(output)


# Function to take arguments from the command line and use them as the input
if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser("Roman Numeral Translator")
    argumentParser.add_argument("--string", type=str, help="Input a Roman Numeral to be translated.")
    argumentParser.add_argument("--integer", type=int, help="Input a decimal, to be translated.")
    parsed = argumentParser.parse_args()
    if parsed.integer:
        main(parsed.integer)
    elif parsed.string:
        main(parsed.string)

