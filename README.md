# Stormgain\_Bot

Full automated bot thats claims the StormGain Miner. For Educational purposes only.

# Instructions

## Prerequisites

* Python 3
* Google Chrome/Chromium
* Selenium ChromeDriver
* A desktop environment

## Setup

### Linux

* Set up a Linux environment with a desktop session or at least a headless desktop. Instructions for the Raspberry Pi [here](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html). (Headless will not work due to CAPTCHA.)
* Clone this repository

```
github clone https://github.com/korewaChino/Stormgain_Bot.git
```

* Install Python 3 (Depends on distribution)<span style="font-family: var(--vscode-editor-font-family); font-size: 1em; font-weight: var(--vscode-editor-font-weight); color: var(--vscode-unotes-wysText);"></span>

```
sudo apt install python3
```

* Install ChromeDriver

```
sudo apt-get install chromium-chromedriver
```

* Install the Python Selenium module

```
   python3 -m pip install selenium 
```

### Windows

* Install Google Chrome (if you have't yet)
* Clone this repository (or download it as ZIP)

```
github clone https://github.com/korewaChino/Stormgain_Bot.git
```

* [Install Python](https://www.python.org/downloads/)
* Install the Python Selenium module

```
   pip install selenium
```

* [Download the ChromeDriver binary](https://chromedriver.chromium.org/) and put it in the same folder.

## Configuration

* Copy `settings-template.json` as `settings.json`
* Run the Python Script

```
python stormgain.py
```

OR

```
python3 stormgain.py
```
