# Learning Beutiful soup
# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()
    

#Beautiful Soup is a Python library for pulling
#data out of HTML and XML files.

# It takes a markup as first argument
# and type of parser as second argument
# (html.parser is python's html parser)
soup = BeautifulSoup(contents, 'html.parser')

print(soup.prettify()) # prints whole html code

print(soup.title) # returns title tag and its content
print(soup.title.name) # name of tag
print(soup.title.string) # returns content of html page

print(soup.a) # first anchor tag