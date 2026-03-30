from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1. Open the Chrome browser using Selenium WebDriver.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 2. Navigate to the website https://www.youtube.com.
driver.get("https://www.youtube.com")

# Step 3. Wait for 2 seconds to allow the page to load.
time.sleep(2)

# Step 4. Maximize the browser window.
driver.maximize_window()

# Step 5. Locate the YouTube search box.
# (Note: YouTube uses the 'name' attribute "search_query" for its search bar)
search_box = driver.find_element(By.NAME, "search_query")

# Step 6. Enter the text "open source software" in the search field.
search_box.send_keys("open source software")

# Step 7. Click the Search button.
# (Note: YouTube uses the 'id' "search-icon-legacy" for the main search button)
search_button = driver.find_element(By.ID, "search-icon-legacy")
search_button.click()

# Step 8. Wait for 5 seconds to view the search results.
time.sleep(5)

# Step 9. Close the browser.
driver.quit()