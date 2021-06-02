class CaptchaError(Exception):
    SystemError('Headless Mode Enabled while captcha exists!')
    SystemExit('CAPTCHA Lock while headless! Exiting...')
        

class noPath:
    SystemExit('OS not recognized and no custom path has been found. Exiting...')

class noCustomPath(Exception):
    print('chromedriver_path not set, assuming default directory by OS...')
    pass
