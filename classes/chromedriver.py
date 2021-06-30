from logging import warn
from user_agent import generate_user_agent
from platform import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import platform
import json
from classes.error import *

with open ('./settings.json') as config_file:
    config = json.load(config_file)


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
        options.add_argument("--user-data-dir=" + path + "/UserData")
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

class driver():
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
        
    finally: driver = webdriver.Chrome(options=options, executable_path=execpath)
