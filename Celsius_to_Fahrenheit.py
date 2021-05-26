#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 25, 2021
# Converts fahrenheit to celsius


def fahrenheit():
    user_input = (input("Enter your temperature in celsius (C°): "))
    try:
        celsius_temp = int(user_input)
        f_temp = (9 / 5) * celsius_temp + 32
        print("{0}C° is {1:.0f}F°".format(celsius_temp, f_temp))
    except Exception:
        print("{} is not a temperature".format(user_input))
    finally:
        print("Done.")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
