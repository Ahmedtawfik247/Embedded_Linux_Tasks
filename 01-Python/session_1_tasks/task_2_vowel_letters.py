#!/usr/bin/python3

#-------------------------------------------------------------------------
#Write a Python program to test whether a passed letter is a vowel or not.
#-------------------------------------------------------------------------


character = input("enter a letter :")
vowels = ['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print(f"the letter in '{character}' is vowel.")
else :
    print(f"the letter in '{character}' is not vowel.")