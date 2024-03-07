Using the python selenium (https://www.cowin.gov.in/)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open the browser and navigate to the website
driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/")

# Click on "Create FAQ" anchor tag
create_faq_link = driver.find_element(By.XPATH, "//a[contains(text(),'Create FAQ')]")
create_faq_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Click on "Partners" anchor tag
partners_link = driver.find_element(By.XPATH, "//a[contains(text(),'partners')]")
partners_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Get window handles (for the home page and the two opened windows)
window_handles = driver.window_handles

# Display the window handles
print("Window Handles:")
for handle in window_handles:
    print(handle)

# Switch to the first opened window (Create FAQ)
driver.switch_to.window(window_handles[1])
print("Window 1 URL:", driver.current_url)

# Switch to the second opened window (Partners)
driver.switch_to.window(window_handles[2])
print("Window 2 URL:", driver.current_url)

# Close the opened windows
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Switch back to the home page
driver.switch_to.window(window_handles[0])

# Close the browser
driver.quit()
