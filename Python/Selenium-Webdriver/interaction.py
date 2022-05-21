from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# enters the article count link
# article_count.click()

# find links using there texts
encyclopedia = driver.find_element(By.LINK_TEXT, value="encyclopedia")
encyclopedia.click()


# search a key by entering into search bar and press enter
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()