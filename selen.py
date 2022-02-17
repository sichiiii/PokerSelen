import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Selen():
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()  
        self.option.add_argument('--disable-dev-sh-usage')
        self.option.add_argument('--disable-gpu')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--headless')
        self.browser = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__)) + '/chromedriver', options=self.option)

    def get_frame(self):
        link = f'https://www.winamax.fr/en/poker/launch_poker.php'
        self.browser.get(link)
        sleep(2)
        frame = self.browser.find_element(By.NAME, 'pokWEB')
        self.browser.switch_to.frame(frame); 
        frame = self.browser.find_element(By.NAME, 'login')
        self.browser.switch_to.frame(frame);
        sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/div/div[1]/div[2]/div[2]/input').send_keys("email")
        self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys("pass")
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/button').click()
        sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/div/div[2]/div[1]/input').send_keys("day")
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/div/div[2]/div[2]/input').send_keys("month")
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/div/div[2]/div[3]/input').send_keys("year")  
        self.browser.find_element(By.XPATH, '//*[@id="mount"]/div[2]/form/button').click()
        sleep()
        frame = self.browser.find_element(By.NAME, 'pokWEB')
        self.browser.switch_to.frame(frame); 
        sleep(2)
        print(self.browser.page_source)
        sleep(500)
        self.browser.quit()

if __name__ == "__main__":
    selen = Selen()
    selen.get_frame()