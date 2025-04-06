from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the YouTube video
video_url = 'https://youtu.be/1227R6KY8Ts'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model

# Path to your ChromeDriver
webdriver_service = Service('C:\Program Files\Google\Chrome\Application\133.0.6943.99\Installer\chrome.7z\Chrome-bin\133.0.6943.993')  # Update this path

# Initialize the WebDriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Open the YouTube video page
    driver.get(video_url)

    # Wait for the title element to be present
    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title yt-formatted-string'))
    )
    title = title_element.text

    # Wait for the description element to be present
    description_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#description yt-formatted-string'))
    )
    description = description_element.text

    # Print the extracted information
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"URL: {video_url}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
