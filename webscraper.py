from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://github.com/GithubNathan")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("LinearRegressionML")
search.send_keys(Keys.RETURN)

ML = driver.find_element_by_id(366758766)

ML.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
