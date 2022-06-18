from scrapper import Scrapper
from sheet import Sheet

# get address, price and links
data = {}
scrapper = Scrapper('https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=1,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=New-Town&cityName=Kolkata&BudgetMin=5000&BudgetMax=15000')
data['address'] = scrapper.get_address()
data['price'] = scrapper.get_price()
data['links'] = scrapper.get_link()

# send data to sheet class and fill the sheet
sheet = Sheet(link='link to spreadsheet', data=data)
# get link to spreadsheet
