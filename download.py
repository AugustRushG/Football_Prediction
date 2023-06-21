import time
from selenium import webdriver

USERNAME = 'Augustrush_gsh' # Your username
PASSWORD = 'Cy*V,-D2ya2.LLc' # Your password
CHROMEDRIVER_PATH = "C://Users//xu741//Downloads//chromedriver_win32//chromedriver.exe" # Insert the path of chromedriver (to be downloaded from "https://sites.google.com/a/chromium.org/chromedriver/downloads")

driver = webdriver.Chrome()

driver.get('https://footystats.org/login')


time.sleep(5) # Let the user actually see something!


search_box = driver.find_element("name",'username')
search_box.send_keys(USERNAME)
search_box = driver.find_element("name",'password')

search_box.send_keys(PASSWORD)



driver.find_element("id",'register_account').submit()

time.sleep(5) # Let the user actually see something!


driver.get('https://footystats.org/c-dl.php?type=matches&comp=3121');  # Sample download 1
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3119');  # Sample download 2
driver.get('https://footystats.org/c-dl.php?type=matches&comp=246')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=12')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=11')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=10')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=9')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=8') # 16/17
driver.get('https://footystats.org/c-dl.php?type=matches&comp=161')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=6')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=5')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=4')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=3')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=2')
driver.get('https://footystats.org/c-dl.php?type=matches&comp=1')


time.sleep(5)


driver.quit()