#!/usr/bin/env python3.9
from logging import debug, error, exception, warn
from user_agent import generate_user_agent
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
from classes.error import *
import sys
from selenium.common.exceptions import NoSuchElementException


with open ('settings.json') as config_file:
    config = json.load(config_file)
stormgainemail = config['stormgain_email']
stormgainpw = config['stormgain_pw']
fromA = config['stormgainsleepMIN']
toB = config['stormgainsleepMAX']


path = os.getcwd()+'\\'
options = Options()
#Launch Arguments
useragent = 'User-Agent=' + generate_user_agent(navigator=["chrome", "firefox"])
arguments = [
        '--no-sandbox',
        useragent,
        '--disable-dev-shm-usage',
        
]
seperator = '\n'
for obj in arguments: #Load every launch argument
     options.add_argument(obj)
options.add_argument(path)

#User Data
try:
    if config['stormgainsleepMAX']:
        options.add_argument("--user-data-dir=" + path + "/UserData/")
except:
    pass
        

options.add_argument('--profile-directory=Profile 1')

if not config['headless_mode']:
    for obj in os.listdir("./extensions"): #Loads all extensions in extensions folder
        print('Loading ' + "./extensions/" + obj)
        options.add_extension("./extensions/" + obj)
else:
    print('Headless Mode on, Extensions disabled.')



#Headless Check
if config['headless_mode']:
    print("Running Headless Mode...")
    options.add_argument('--headless')


class browserstarter:

    def start(self):
        try:

        
            if not "chromedriver_path" in config:
                warn("chromedriver_path not set, assuming default directory by OS...")
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
                    raise noPath(Exception)
                
            else:
                execpath = config['chromedriver_path'] #Exact Path, No relative path allowed
            
        finally: self.driver = webdriver.Chrome(options=options, executable_path=execpath)
        
        #Clear Check
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        print("Using Agent: " + useragent)
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
        print('Cooldown!\nClose Browser!')
        self.driver.close()
        ran = randint(600, 1800)
        print("Sleep:",int(ran),"seconds")
        time.sleep(ran)
        start.start()
        
    def countdownSleep(self):
        print('countdown')
        countdown = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/div[3]/div/div[1]/span[2]').get_attribute('innerHTML')
        if countdown == 'Synchronizing': start.countdownSleep()
        print(countdown)
        time_converted = sum(x * int(t) for x, t in zip([3600, 60, 1], countdown.split(":"))) + 30        
        print('Going to sleep from countdown time + 30s...!\nClose Browser!')
        self.driver.close()
        print("Sleep:",countdown,"")
        time.sleep(time_converted)
        start.start()

    def claimusdt(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        except Exception as e:
            print(e)

    def checkusdt(self):
        try:
            #time.sleep(3)
            print('checking USDT')
            html = self.driver.find_element(By.CSS_SELECTOR, '#region-main > div > div:nth-child(2) > div > div.env > div > div > div:nth-child(2) > div.text-gray-1.text-13.md-text-15.leading-4.md-leading-24.text-center > span:nth-child(1)').get_property("innerHTML")
            usdt = html.replace('≈','')
            print('You have Mined '+str(usdt)+'$')
            if float(usdt) >= float(10):
                print('More Than 10USDT, Claim it now!')
                start.claimusdt()
        except Exception as e:
            print(e)

    def stormgain(self):
        try:
            
            self.driver.get("https://app.stormgain.com/crypto-miner/") #Check Website
            #time.sleep(randint(3,6))
            
            try:
                try:
                    login = self.driver.find_element(By.CLASS_NAME, "login-view").is_displayed() #Check for Login Page
                except NoSuchElementException: 
                    return False
                pass

                if login:

            
                    #pass
                    #commit le login
                    #self.driver.get("https://app.stormgain.com/#modal_login")
                    debug('Logging in...')     
                    #time.sleep(randint(3,6))
                    self.driver.find_element(By.ID, "email").send_keys(stormgainemail)
                    debug('Inserting Email...')
                    self.driver.find_element(By.ID, "password").send_keys(stormgainpw)
                    debug('Inserting Password...')
                    self.driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
                    debug('Clicking Login...')
                    

                try:
                    login = self.driver.find_element(By.CLASS_NAME, "login-view").is_displayed()
                except NoSuchElementException: 
                    return False
                if login:
                    self.driver.find_element(By.CSS_SELECTOR, ".btn-login").click();
                    if self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/form/div[5]"):
                        print(self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/form/div[3]/div").innerHTML)
                        print('Captcha Detected!')
                        if config['headless_mode'] == True:
                            raise CaptchaError(Exception)
                        else:
                            print('Captcha Detected')
                            while not self.driver.find_element(By.CSS_SELECTOR, "#recaptcha-anchor > div.recaptcha-checkbox-checkmark"):
                                time.sleep(1)
                    else:
                        error(self.driver.find_element(By.CSS_SELECTOR,"#modal > div > div.modal-content > form > div.msg-error-wrapper").innerHTML)
            except NoSuchElementException:
                print('No need to login! Great!')                                       
        finally:    
            #self.driver.get('https://app.stormgain.com/crypto-miner/')
            #time.sleep(5)
            start.checkusdt()      
            try:
                time.sleep(3)
                self.driver.find_element(By.CSS_SELECTOR, ".font-medium > .text-17").click()
                time.sleep(randint(3,6))
                start.stormgainsleeper()
            except NoSuchElementException:
                print('Currently Mining...')
                try:
                    #time.sleep(5)
                    start.countdownSleep()
                except:

                    start.shortsleep()
                if KeyboardInterrupt:
                    exit()

start = browserstarter()
start.start()
