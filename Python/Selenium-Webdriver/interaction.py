import imp
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.ID, value="articlecount")
count = article_count.text.split(' ')
print(count[0])

driver.quit()