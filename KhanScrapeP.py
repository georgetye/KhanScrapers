from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/is-obesity-contagious-"
driver = webdriver.PhantomJS()
driver.get(url)
time.sleep(3.5)

elem = driver.find_element_by_xpath("//*")
source = elem.get_attribute("outerHTML")

soup = BeautifulSoup(source, 'html.parser')

print(soup)

#if found == True:
#	passageSource += str(soup.find("div", {"data-reactid":".3.$"+x}))
#	print(passageSource)

#soup = BeautifulSoup(passageSource)
#passageText = soup.get_text()

#print(passageText)
