#python exerciese
#https://www.ynonperek.com/2017/09/21/python-exercises/
import sys
#1. write a program to take a task that ask user for a number and prints the sum
# ot its digits. (int)
#2. wreite a program that takes a file name as command line argument, count how
#many times each word appears in the file and prints the word that appears the
#most


class solution(object):
    """Exercise object"""
    def sumdigits(self):
        """Exercise 1"""
        try:
            intP = int(input('Enter your number: '))
        except ValueError:
            print('Please Enter an integer: ')
            sys.exit()

        strP = str(intP)
        l = []
        for char in strP:
            l.append(int(char))
        self = sum(l)
        print(self)
    def countwords():
        """Exercise 2"""


s = solution()
s.sumdigits()







