from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Initialize GeckoDriver service
service = Service("C:\\WebDriver\\geckodriver.exe")  # Ensure this path is correct
driver = webdriver.Firefox(service=service)

# Open Amazon Associates login page
driver.get("https://affiliate-program.amazon.com/")
time.sleep(5)

# Navigate to the product page
product_url = "https://www.amazon.com/dp/B08N5WRWNW"
driver.get(product_url)
time.sleep(5)

# Find and click the SiteStripe link
try:
    site_stripe = driver.find_element(By.ID, "amzn-ss-text-link")
    site_stripe.click()
    time.sleep(3)

    # Get the generated affiliate link
    affiliate_link = driver.find_element(By.ID, "amzn-ss-text-shortlink-textarea").get_attribute("value")
    print(f"Affiliate Link: {affiliate_link}")

except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()
