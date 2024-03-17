from selenium import webdriver

# declaring ChromeOptions class using webdriver package and craeting a object
# using its object, call method add_argument to pass "headless" as argument
# add another flag to ignore certificate errors on webpage.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Selenium supports  Running javascript in python to handle scroll event.
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#  to click a screenshot of current browser mode and save it in file.
driver.get_screenshot_as_file("screen.png")

