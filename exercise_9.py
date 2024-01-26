# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 9:
# Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# create a function
def check_if_palindrome(number):
    original_number = str(number)
    reversed_number = original_number[::-1]

    if original_number == reversed_number:
        print(f"The given number {original_number} \nYes, it's a palindrome number")
    else:
        print(f"The given number {original_number} \nNo, is not a palindrome")

# check if working
check_if_palindrome(13578)
check_if_palindrome(32123)