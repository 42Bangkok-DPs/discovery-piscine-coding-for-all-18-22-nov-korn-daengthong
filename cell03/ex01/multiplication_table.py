#!/usr/bin/env python3
def main():
    number = int(input("Enter a number:\n"))

    for i in range(10):
        print(f"{i} x {number} = {i * number}")

if __name__ == "__main__":
    main()