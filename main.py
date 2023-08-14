# ------------------------------------- ISP - TWITTER BOT --------------------------------- #

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

PROMISED_DOWN = 40
PROMISED_UP = 30
TWITTER_EMAIL = 'your_mail@gmail.com'
TWITTER_USERNAME = 'your_username'
TWITTER_PASSWORD = 'your_password'

OPTIONS = Options()
OPTIONS.add_experimental_option('detach', True)

CHROME_DRIVER_PATH = "your_chrome_driver_path"
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=OPTIONS)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        go = self.driver.find_element(by=By.CSS_SELECTOR, value='.start-button a')
        go.click()
        time.sleep(50)
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print("Down: ", self.down)
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("Up: ", self.up)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(2)
        email = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        username = self.driver.find_element(by=By.NAME, value='text')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(1)
        draft = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        draft_text = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? \n\n Just testing the code !!"
        draft.send_keys(draft_text)
        time.sleep(10)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

        


