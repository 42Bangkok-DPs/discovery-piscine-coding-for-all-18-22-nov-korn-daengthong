#!/usr/bin/env python3

def main():
    first_number = float(input("Give me the first number: "))
    
    second_number = float(input("Give me the second number: "))
    
    print("Thank you!")
    
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} / {second_number} = {first_number / second_number}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")

if __name__ == "__main__":
    main()