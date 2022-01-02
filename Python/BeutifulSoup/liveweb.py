# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# live web used: https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/" )
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
article_tags = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for tag in article_tags:
    text = tag.get_text()
    link = tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_score_tags = [
    int(tag.getText().split()[0]) 
    for tag in soup.find_all(name="span", class_="score")
    ] 

largest=max(article_score_tags)
largest=article_score_tags.index(largest)

print(f"Most Upvoted article is: {article_texts[largest]}\nLink: {article_links[largest]}\nIt has {article_score_tags[largest]} upvotes")

#print(article_links)
#print(article_score_tags)

