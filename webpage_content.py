from selenium import webdriver

# Set the path to your webdriver executable (make sure to download the appropriate driver for your browser)
webdriver_path = '/path/to/chromedriver'

# Set up the webdriver
driver = webdriver.Chrome(webdriver_path)

# Navigate to the webpage
url = 'https://www.saucedemo.com/'
driver.get(url)

# Extract the entire content of the webpage
page_source = driver.page_source

# Close the webdriver
driver.quit()

# Save the content to a text file
output_file_path = 'Webpage_task_11.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(page_source)

print(f'The content has been saved to {output_file_path}')