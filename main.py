from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Open Google.com
driver.get("https://www.ligaportal.at/regionalliga-ost/analysen/spieler-der-runde/13506-regionalliga-ost-waehle-den-beliebtesten-spieler-der-herbstsaison-2023")

# Locate the search bar element and perform a click action
search_bar = driver.find_element(By.NAME, "q")  # Assuming the search bar has the name attribute "q"
search_bar.click()

# Close the browser window
driver.quit()