#!/usr/bin/env python3

def main():
    # Prompt the user for a number
    user_input = input("Give me a number: ")

    # Try converting the input to a float
    try:
        number = float(user_input)
        
        # Check if the number is an integer
        if number.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("That is not a valid number.")

if __name__ == "__main__":
    main()