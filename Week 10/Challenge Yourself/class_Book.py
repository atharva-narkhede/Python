#Create a Book class that has two attributes :
#title
#author
#two methods:
#1.A method named .get_title() that returns: 'Title: ' + the instance title.
#2.A method named .get_author() that returns: 'Author: ' + the instance author.



class Book:

	def __init__(self, title, author):
		self.title = title
		self.author = author
		
	def get_title(self):
		return 'Title: ' + self.title
		
	def get_author(self):
		return 'Author: ' + self.author
title=input()
author=input()
book1=Book(title,author)
print(book1.get_title())
print(book1.get_author())
