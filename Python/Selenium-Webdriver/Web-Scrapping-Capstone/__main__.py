###############################################################################
# GETTING RENT PROPERTY AT NEW TOWN, KOLKATA, WITHIN 5000-15000 PRICE RANGE   #
# FILLING THE DATA IN GOOGLE FORM TO CREATE A SHEET                           #
#                                                                             #
# BS4 and SELENIUM WEBDRIVER IS USED                                          #
###############################################################################

from scrapper import Scrapper
from sheet import Sheet

import warnings
warnings.filterwarnings('ignore')

# get address, price and links
data = {}
scrapper = Scrapper('https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=1,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&Locality=New-Town&cityName=Kolkata&BudgetMin=5000&BudgetMax=15000')
data['address'] = scrapper.get_address()
data['price'] = scrapper.get_price()
data['links'] = scrapper.get_link()

# send data to sheet class and fill the sheet
sheet = Sheet(url='https://docs.google.com/forms/d/e/1FAIpQLSdNINWR5ucWoULxZsiuCBz-PkVnq49VJ7q22p7Gg19LoS3GXQ/viewform?usp=sf_link')
sheet.create_sheet(data=data)