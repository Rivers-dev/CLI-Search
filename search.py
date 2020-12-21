from selenium import webdriver

options = webdriver.FirefoxOptions()
q = False

while not q:
    print()
    x = input('Enter search query or "q" to quit: ')
    if x == 'q':
        q = True
        continue
    else:
        x = x.replace(' ', '+')
        driver = webdriver.Firefox(firefox_options = options, executable_path=rPATH)
        for i in range(1): 
            driver.get("https://www.google.com/search?q=" + x + "&start=" + str(i)) 
driver.close()