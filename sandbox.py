from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.khanacademy.org/test-prep/mcat/social-sciences-practice/social-science-practice-tut/e/race--socioeconomic-status--and-nutrition"
driver = webdriver.PhantomJS()
driver.get(url)
time.sleep(5)

elem = driver.find_element_by_xpath("//*")
source = elem.get_attribute("outerHTML")


soup = BeautifulSoup(source, 'html.parser')
print(soup)

for x in range (0,9):
	tag = ".4.$"
	tag+= str(x)
	print(tag)
	passageSource = str(soup.find("div", {"data-reactid":tag}))
	numberSoup = BeautifulSoup(passageSource, 'html.parser')
	for tag in numberSoup.find_all("annotation", {"encoding":"application/x-tex"}):
		tag.decompose()
	for span in numberSoup.find_all("span", {"class":"mord"}):
		span.decompose()
	for tag in numberSoup.find_all("mn"):
		tag.decompose()
	for tag in numberSoup.find_all("mi"):
		tag.decompose()
	for tag in numberSoup.find_all("mo"):
		tag.decompose()
	
	image = ''
	
	for images in numberSoup.find_all('img'):
		image = images.get('src')

	numberSoup = str(numberSoup)
	numberSoup = numberSoup.replace(', percent','%')
	numberSoup = numberSoup.replace('is greater than or equal to', '')
	passageSoup = BeautifulSoup(numberSoup, 'html.parser')
	#print(numberSoup)
	passage = passageSoup.get_text()

	if image != '':
		passage += '<img src ="' + image + '">'

	print("x = "+ str(x) + ": " + passage)


