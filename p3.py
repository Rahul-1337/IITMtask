'''
Letter Combinations of a Phone Number


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 
Test case 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Test case 2:
Input: digits = ""
Output: []


Test case 3:
Input: digits = "2"
Output: ["a","b","c"]

'''

from itertools import product

def letter_combinations(phone_number):
    if not phone_number:
        return []

    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    digit_list = [digit_to_letters[digit] for digit in phone_number]

    combinations = [''.join(combination) for combination in product(*digit_list)]

    return combinations
