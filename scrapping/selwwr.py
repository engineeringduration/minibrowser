from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager  # Auto-manages ChromeDriver

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Runs Chrome in headless mode (no GUI)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver service
chrome_driver_path = r"R:\minibrowser\scrapping\chrome_driver-win64\chromedriver.exe"  # Ensure correct path
try:
    service = Service(chrome_driver_path)  # Use local path
except:
    service = Service(ChromeDriverManager().install())  # Auto-download correct ChromeDriver

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the website
url = "https://weworkremotely.com/categories/remote-programming-jobs"
driver.get(url)

# Wait for JavaScript to load
driver.implicitly_wait(5)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract job titles
job_titles = soup.find_all("span", class_="title")

# Print job titles
if job_titles:
    for job in job_titles:
        print(job.text.strip())
else:
    print("No job titles found. Check if the website structure has changed.")

# Close the browser
driver.quit()

