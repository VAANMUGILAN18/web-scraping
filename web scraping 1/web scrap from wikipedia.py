from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

# Search for "hitler"
search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("hitler")
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "mw-headline")))

# Get the headlines
results = driver.find_elements(By.CLASS_NAME, "mw-headline")
headlines = [headline.text for headline in results]

# Write the headlines to a CSV file
csv_filename = "headlines.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Headline"])

    for headline in headlines:
        csv_writer.writerow([headline])

# Click on the link for "Heinrich Himmler"
try:
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Heinrich Himmler")))
    link.click()
except Exception as e:
    print(f"Error clicking the link: {e}")

# Additional actions or assertions as needed

# Close the browser
driver.quit()
