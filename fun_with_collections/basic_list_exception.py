"""
Program basic_list.py

Author: Greg Wilhelm

Last date modified: 03/04/2020

This is just a simple list builder taking in a integer entered by the user and creating a list by repeating the value
three times.

"""

def get_input():
    user_input = int(input("Please enter a number: "))
    return user_input


def make_list():
    inputs = []
    try:
        value = int(get_input())
        for i in range(3):
            inputs.insert(i, value)
        return inputs
    except ValueError:
        print("Invalid type.")


if __name__ == '__main__':
    list_built = make_list()
    print(list_built)
