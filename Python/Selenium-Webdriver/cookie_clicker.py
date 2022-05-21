import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

UPGRADES = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory', 'buyGrandma', 'buyCursor']

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# a bot to click cookie as fast as possible
start_time = time.time()
game_start_time = time.time()
while True:
    cookie = driver.find_element(By.ID, value='cookie')
    cookie.click()
    ref_time = time.time()
    
    if abs(ref_time - start_time) >= 5:
        start_time = ref_time
        time.sleep(0.1)
        # get current score
        upgrade = 0
        while upgrade < len(UPGRADES):

            current_score = driver.find_element(By.ID, value='money')
            current_score = int(current_score.text.strip().replace(',', ''))
            
            required_money = driver.find_element(
                By.XPATH, value='//*[@id="{0}"]/b'.format(UPGRADES[upgrade])
            )

            required_money = int(
                required_money.text.split('-')[1].strip().replace(',', '')
            )
            if current_score >= required_money:
                # click on upgrade
                upgrade_button = driver.find_element(
                    By.XPATH, value='//*[@id="{0}"]'.format(UPGRADES[upgrade])
                )
                upgrade_button.click()
                break
            upgrade += 1
            

    current_time = time.time()
    if current_time - game_start_time >= 300:
        time.sleep(0.1)
        cookie_rate = driver.find_element(By.ID, value='cps')
        print(cookie_rate.text)
        break

driver.quit()