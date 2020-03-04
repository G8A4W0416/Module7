"""
Program file_io.py

Author: Greg Wilhelm

Last date modified: 03/04/2020

The purpose of this program is to prompt the user (teacher) to enter in as many test scores for each student as needed
and write the data to a text file. They can enter 'S' to stop entering scores for the student which will then write
the student name and scores on one line and prompt the user to enter another student and scores if they want or quit the
program.

"""

import os as os


def write_to_file(*args):
    with open('student_info.txt', 'a') as file:
        file.writelines(args)


def get_student_info(**kwargs):
    student_first_name = kwargs.get("student_first_name")
    student_last_name = kwargs.get("student_last_name")
    student_full_name = student_last_name + ", " + student_first_name + " "
    scores = []

    user_input = input("Enter as many scores as you want between 0-100. Enter 'S' to stop: ")
    while user_input != 'S':
        try:
            test_score = int(user_input)
            if 0 <= test_score <= 100:
                scores.append(test_score)
            else:
                print('Please enter a value between 0-100')
            user_input = input("Enter as many scores as you want between 0-100. Enter 'S' to stop: ")
        except ValueError:
            print('Please enter a value between 0-100')
            user_input = input("Enter as many scores as you want between 0-100. Enter 'S' to stop: ")

    scores = str(scores).strip('[]') + '\n'

    write_to_file(student_full_name, scores)


def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"

    with open(os.path.join(file_dir, file_name), "r") as file:
        print(file.read())


if __name__ == '__main__':
    print("Welcome to grade book! This program helps you keep records of your students grades.\n")
    student_first_name_input = input("Enter student's first name. Enter 'Quit' to quit: ").strip()
    while student_first_name_input != "Quit":
        if student_first_name_input == "":
            student_first_name_input = input("Enter student's first name. Enter 'Quit' to quit: ").strip()
        else:
            student_last_name_input = input("Enter student's last name. Enter 'Quit' to quit: ").strip()
            while student_last_name_input != "Quit":
                if student_last_name_input == "":
                    student_last_name_input = input("Enter student's last name. Enter 'Quit' to quit: ").strip()
                else:
                    # We know at this point the first name and last name fields have been filled out and the Quit
                    # command has not been issued. Proceed the user to entering test scores for the student. Once the
                    # user has stopped entering scores, break out of while loop and allow them to enter another student
                    # record. First name and last name are re-validated.
                    get_student_info(student_first_name=student_first_name_input,
                                     student_last_name=student_last_name_input)
                    break

            student_first_name_input = input("Enter student's first name. Enter 'Quit' to quit: ").strip()

    read_from_file()
    input("Press any key to end")
