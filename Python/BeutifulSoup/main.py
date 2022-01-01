# Learning Beutiful soup
# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from os import name
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

# returns all of the tags which is provided(a,p,hr,etc)
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText()) # returns text of the tags
    print(tag.get("href")) # returns tag attribute value
    

# find returns only one instance of tag
# we can pass it's attribute value also to get hold of any
# specific tag    
# NOTE: Since class is a keyword in python
#       to use class attribute we use class_
heading = soup.find(name="h1", id="name") # here h1's attribute is id
print(heading)


# select_one: gives first matching item
# select: fives all of the matching items

# here it selects first anchor tag inside p tag
# it works like css selectors
company_url = soup.select_one(selector="p a") 
print(company_url)

# selects as per id name
name = soup.select_one(selector="#name")
print((name))

# selects all the items with heading class
headings = soup.select(selector=".heading")
print(headings)