from platform import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import platform
import json
from  random import randint

with open ('settings.json') as config_file:
    config = json.load(config_file)
stormgainemail = config['stormgain_email']
stormgainpw = config['stormgain_pw']
fromA = config['stormgainsleepMIN']
toB = config['stormgainsleepMAX']
path = os.getcwd()+'\\'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(path)



class browserstarter:

    def start(self):
        try:
            if "chromedriver_path" in config:
                execpath = path+ config['chromedriver_path']
            else:
                raise Exception
        except:
            print("chromedriver_path not set, assuming default directory by OS...")
            #OS Check
            ##Windows
            if platform.system() == 'Windows':
                execpath = path +"\\chromedriver.exe"
            #macOS
            elif platform.system() == 'Darwin':
                execpath = '/usr/local/bin/chromedriver'
            ##Linux
            elif platform.system() == 'Linux':
                execpath = '/usr/bin/chromedriver'
            ##None Detected
            else:
                raise SystemExit('OS not recognized and no custom path has been found. Exiting...')
        
            
        self.driver = webdriver.Chrome(options=chrome_options, executable_path=execpath)
        
        #Clear Check
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
        print("Browser started!")
        start.stormgain()

    def startup(self):
        start.start()

    def stormgainsleeper(self):
        sleeptime = randint(fromA, toB)
        self.driver.close()
        print('Miner is Active!\nNext Claim in',sleeptime, 'sec')
        time.sleep(sleeptime)
        start.start()


    def shortsleep(self):
        print('Short Sleep Triggered!\nClose Browser!')
        self.driver.close()
        ran = randint(600, 1800)
        print("Sleep:",int(ran),"sec")
        time.sleep(ran)
        start.start()

    def claimusdt(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        except Exception as e:
            print(e)

    def checkusdt(self):
        try:
            html = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/span[1]').get_attribute('innerHTML')
            usdt = html.replace('≈','')
            print('You have Mined '+str(usdt)+'$')
            if float(usdt) >= float(10):
                print('More Than 10USDT, Claim it now!')
                start.claimusdt()
        except Exception as e:
            print(e)

    def stormgain(self):
        try:
            self.driver.get("https://app.stormgain.com/#modal_login")
            print('Logging in...')     
            time.sleep(randint(3,6))
            self.driver.find_element(By.ID, "email").send_keys(stormgainemail)
            print('Inserting Email...')
            self.driver.find_element(By.ID, "password").send_keys(stormgainpw)
            print('Inserting Password...')
            time.sleep(randint(3,6))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
            print('Clicking Login...')
            time.sleep(randint(3,6))
            self.driver.get('https://app.stormgain.com/crypto-miner/')
            time.sleep(randint(3,10))
            #self.driver.switch_to.frame(0)
            start.checkusdt()
            #self.driver.refresh()
            time.sleep(randint(3,10))
            #self.driver.switch_to.frame(0)
        except:
            start.shortsleep()
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".font-medium > .text-17").click()
            time.sleep(randint(3,6))
            print('Miner is Active!')
            start.stormgainsleeper()
        except:
            print('Mining already active?\nGetting Short Sleep!')
            start.shortsleep()
            if KeyboardInterrupt:
                exit()

start = browserstarter()
start.start()
