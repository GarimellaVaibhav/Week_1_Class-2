# -*- coding: utf-8 -*-
"""Copy of 02-ListsTuples_Lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_Ro0T66ytgS-8IJ0tlAQweWIdQSeJfT

# Lab Exercise 

Complete the questions below as part of the Lab exercises.

# Part 1

After running the starter code, complete the questions below.
"""

# STARTER CODE 1
! pip install newspaper3k

# STARTER CODE 1
from newspaper import Article
URL = "https://www.boston.com/travel/travel/2020/09/16/best-apple-orchard-according-to-readers"
article = Article(URL)
article.download()
article.parse()
article_text = article.text

# Q1: print out the article_text variable. This is the variable we will be using.

print(article_text)

# Q2: how many times does the word apple appear across any case (upper or lower)?

substring ="apple"
lowercase=article_text.lower()
count = lowercase.count(substring)
print("The word 'apple' has appeared", count," times")

# Q3: how many individual words are there?
# TRICKY:  Look at the string methods
# Also an opportunity to think about how you might search for help to a problem, 
# search engines are our friend.
listRes = article_text.split(" ")
print(listRes)
print("There are ",len(listRes),"number of words")

# Q4:  Building on the solution above, create a list where each entry is a sentence.
# use "." to define a sentence.
listRes2 = article_text.split(".")
print(listRes2)
print("There are ",len(listRes2),"number of sentences")

# Q5: How many characters are there in article_text
print("There are",len(article_text),"characters")

# Q6: subset article_text to include only the first 100 characters
listRes = article_text.split(" ")
print(str(listRes[0:100]))

"""# Part 2"""

# STARTER CODE SNIPPET

# our list
our_list = [1,2,3,4,5, ['a', 'b', 'c'], 6, 7, 8, 9, 10]

# Q1:  What is the length of the object/variable our_list?
len(our_list)

# Q2: Append the number 11 to the end of the list
our_list.append(11)
print(our_list)

# Q3: remove the 11 you just added in Q2
our_list.remove(11)
print(our_list)

# Q4: Create a list that only contains the list of letters
# call this variable letters
variable_letters=["a","b","c","d","e"]

# reverse the variable letters
print(variable_letters)
variable_letters.reverse()
print(variable_letters)

