from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Initialize the browser
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.maximize_window()
driver.implicitly_wait(10)

# Step 2: Open the input page
driver.get("https://agrichain.com/qa/input")

# Step 3: Enter string input (Assuming input box has id='string-input')
input_box = driver.find_element(By.ID, "string-input")
input_box.send_keys("abcabcbb")

# Step 4: Click the submit button (Assuming button has id='submit-btn')
submit_button = driver.find_element(By.ID, "submit-btn")
submit_button.click()

# Step 5: Wait for result page and capture output (Assuming output has id='output-result')
time.sleep(2)  # small wait for page load
output = driver.find_element(By.ID, "output-result").text

# Step 6: Validate the output
expected_output = "3"
assert output == expected_output, f"Test Failed: Expected {expected_output}, but got {output}"
print("Test Passed: Output is", output)

# Step 7: Close the browser
driver.quit()
