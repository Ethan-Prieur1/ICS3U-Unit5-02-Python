#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that finds the area of a triangle


def calculate_area(base, height):
    # Calculate area

    # Process
    area = base * height / 2

    # Output
    print("The area of the triangle {0} cm²".format(area))


def main():
    # This is the main function

    # Input
    user_base = input("Enter Base of the triangle (cm): ")
    user_height = input("Enter Height of the triangle (cm): ")
    print("")

    # Process
    try:
        height_int = int(user_height)
        base_int = int(user_base)
        # Call Functions
        calculate_area(base_int, height_int)
    except Exception:
        print("That's not an integer dinghead.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
