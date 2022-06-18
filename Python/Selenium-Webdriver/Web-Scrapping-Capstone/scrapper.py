import requests

from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, link: str) -> None:
        self.soup = BeautifulSoup(self.get_html(link), "html.parser")
        
    def get_html(self, link):
        response = requests.get(link)
        return response.text
    
    def get_address(self):
        addresses = self.soup.find_all(name='h2', class_="mb-srp__card--title")
        address_list = []
        for address in addresses:
           address_list.append(address.get_text())
        return address_list
    
    def get_price(self):
        prices = self.soup.find_all(name='div', class_="mb-srp__card__price--amount")
        price_list = []
        for price in prices:
            price_list.append(price.get_text())
        return price_list
    
    def get_link(self):
        links = self.soup.find_all(itemprop="url")
        link_list = []
        for link in links:
            link_list.append(link['content'])
        return link_list