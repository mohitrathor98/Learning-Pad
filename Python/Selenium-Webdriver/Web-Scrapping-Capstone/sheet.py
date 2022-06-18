from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Sheet:
    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = url

    def create_sheet(self, data):
        total_data = len(data['address'])
        for i in range(total_data):
            self.driver.get(self.url)
            sleep(3)
            try:
                address_element = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                address_element.send_keys(data['address'][i])
            
                price_element = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price_element.send_keys(data['price'][i])
            
                links_element = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                links_element.send_keys(data['links'][i])

                button = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
                button.click()
                
            except Exception as e:
                raise e
            