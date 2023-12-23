from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
class Hariom:
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))




   def __init__(self, url):
       self.url = url


   # starting point
   def booting_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           return False
           print("ERROR : Unable to run the code !")


   # shutdown method - to close the Python Selenium automation
   def shutdown(self):
       if self.booting_function() == True:
           self.driver.quit()
       else:
           return False


   # fetch the title of the web application
   def fetch_title(self):
       if self.booting_function() == True:
           return self.driver.title
       else:
           return False


       # fetch the URL of the web application


   def fetch_url(self):
       if self.booting_function() == True:
           return self.driver.current_url
       else:
           return False


       # fetch the entire source code of the webpage


   def fetch_webpage(self):
       if self.booting_function() == True:
           return self.driver.page_source
       else:
           return False




url = "https://www.saucedemo.com/"


hariom = Hariom(url)
print("Title of {a} = ".format(a="Demo"),hariom.fetch_title())
print()
print("URL of {a} : ".format(a="Demo"),hariom.fetch_url())
print()
print(hariom.fetch_webpage())
hariom.shutdown()