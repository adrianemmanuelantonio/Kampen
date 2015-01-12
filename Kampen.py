#!/usr/bin/python
'''
Title: Kampen's Method
Author: Adrian Emmanuel M. Antonio
Date: March 30, 2014
Description: Program to count number of words from given input
'''
class Kampen(object):	
	self.count = 0
	self.result = 0
	def __init__(self, inputWord, count2, toSearch):
		self.inputWord  = inputWord
		self.count2 = count2
		self.toSearch = toSearch
		self.counter()
	def counter(self):
	    for loop in inputWord:
	        if inputWord[self.count:self.count2] == self.toSearch:
	            self.result = self.result + 1
	        self.count = self.count + 1
	        self.count2 = self.count2 + 1
	    return self.result
inputWord = input("Enter a long word: ")
searchWord = input("Enter word to be searched: ")
wordLength = len(searchWord)
kampen = Kampen(inputWord, wordLength, searchWord)
result = kampen.counter()
print("Words found is: {0}".format(result))