from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# To keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

wait = WebDriverWait(driver, 10)
price_element_rupee = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
price_element_paisa = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-fraction")))

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"Price: {price_element_rupee.text}.{price_element_paisa.text}")
# Xpath
pot_store_link = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bylineInfo"]')))
print(pot_store_link.text)
# ID
product_title = wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
print(product_title.size)
# Also can use find_elements to find every element in the source code

driver.quit()
