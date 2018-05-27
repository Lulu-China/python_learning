#!/usr/bin/env Python
# coding=GBk

import codecs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
	driver = webdriver.Firefox(executable_path="geckodriver")
	driver.maximize_window()
	
	#打开登录页面
	driver.get("http://www.baidu.com") 
	
	#打开超链接 新闻
	news = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')
	news.click()
	
	#获取新闻列表
	news_ul = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul'))
	# while True:
		# try:
			# news_ul = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul')
			# break
		# except:
			# print "get failed"

	news_lis = news_ul.find_elements_by_tag_name('li')
	
	file=u"百度新闻.txt"
	f=codecs.open(file,'w', "GB18030")
	for li in news_lis:
		print "xxxx="+li.text
		f.write(li.text+"\r\n")
	f.close()
