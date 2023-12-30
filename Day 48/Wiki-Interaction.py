from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# articles.click()

# portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Arun")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("S")
email = driver.find_element(By.NAME, "email")
email.send_keys("test@gmail.com")
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()