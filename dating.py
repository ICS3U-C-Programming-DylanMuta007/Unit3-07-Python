#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program decide if you are going to marry my daughter or not using logic operations


def main():
    # Asks user to enter an integer
    age_as_string = input("Tell me your age young lad: ")
    print("")

    try:
        # Converts string to int
        age_as_int = int(age_as_string)

        # If the age is  older than 25 and younger than 40 he is allowed to marry
        if age_as_int >= 25 and age_as_int <= 40:
            print("Welcome to the family young lad")

        # If less than 0 or more than 100 it stares at you
        elif age_as_int < 0 or age_as_int > 100:
            print("._.")

        # If less than 25 he is too young
        elif age_as_int < 25:
            print("I'm sorry but your too young lad")

        # if more than 40 he is too old
        elif age_as_int > 40:
            print("your too old lad")

        # If less than 0 or more than 100 it stares at you
        elif age_as_int < 0 or age_as_int > 100:
            print("._.")

    # If the error occurs whole converting runs exception
    except Exception:
        print(age_as_string, "is not a number young lad. Try again")

    # Final
    finally:
        print("")
        print("Thanks for paying :)")


if __name__ == "__main__":
    main()
