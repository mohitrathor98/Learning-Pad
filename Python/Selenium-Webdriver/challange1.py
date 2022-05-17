import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.python.org')

elements = driver.find_elements(
        by=By.XPATH, 
        value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul'
    )

event_details = elements[0].text
event_details = event_details.splitlines()

event_details_dict = {}
sl_no = 0
for index in range(0, len(event_details), 2):
    event_details_dict[sl_no] = {
        event_details[index]:event_details[index+1]
    }
    sl_no += 1

print(json.dumps(event_details_dict, indent=4))

driver.quit()