from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# ChromeDriverManager installs chrome web driver
# and driver handles chrome browser now
driver = webdriver.Chrome(ChromeDriverManager().install())

# gets the url and opens it in chrome
driver.get("https://www.amazon.in/dp/B09M742LJT/ref=sspa_dk_detail_0?pd_rd_i=B09M742LJT&pd_rd_w=dzY1v&pf_rd_p=4e9225d2-7473-4eb0-95d5-670190275218&pd_rd_wg=hJscP&pf_rd_r=K1JAZKJW8FMKCWMPF7G7&pd_rd_r=baa31a8d-85ed-46f0-bc86-67ef3ce205a9&s=electronics&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTzhRV0Q1Tk05V0RSJmVuY3J5cHRlZElkPUEwNzU5OTk5QUg3TTdQTzhLRFM0JmVuY3J5cHRlZEFkSWQ9QTA0MzQ3MDQxVDNZTUhTQVk1QTZQJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")

# find an element by using its id
price = driver.find_element_by_id('corePriceDisplay_desktop_feature_div')
print(price.text) # get text

# find an element by using its name attribute of the tags
search_bar = driver.find_element(by=By.NAME, value="field-keywords")
print(search_bar.tag_name)
print(search_bar.get_attribute('type'))

# find element using css selectors
logo = driver.find_element(by=By.CSS_SELECTOR, value='#nav-logo a')
print(logo.size)

# x path := XPath uses "path like" syntax to identify and navigate nodes
price = driver.find_element(by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
print(price.text)

# closes the browser
driver.quit()