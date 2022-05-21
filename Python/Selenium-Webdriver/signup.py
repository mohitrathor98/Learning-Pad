from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Mohit")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Rathor")

email = driver.find_element(By.NAME, value="email")
email.send_keys("mohit.demo@gmail.com")

submit = driver.find_element(By.TAG_NAME, value="button")
submit.click()

driver.quit()
