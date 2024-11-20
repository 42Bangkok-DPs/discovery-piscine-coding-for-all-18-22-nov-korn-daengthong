#!/usr/bin/env python3

def main():
    number = float(input("Enter a number: "))
    
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

if __name__ == "__main__":
    main()