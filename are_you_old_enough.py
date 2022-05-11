#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a greater than less than

import random


def main():

    # This is a greater than less than, with try and catch

    # input
    age = input("Enter your age here! : ")

    # process & output
    try:
        age_number_string = int(age)

        if age_number_string >= 25 and age_number_string <= 40:
            print("\nYou're a good age!")
        else:
            print("\nYou're not a good age!")

    except Exception:
        print("\nThat was not an integer")
    print("\nDone.")


if __name__ == "__main__":
    main()
