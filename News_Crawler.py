#!/usr/bin/env Python
# coding=gb18030

import sys
import time
import codecs
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf-8')

def SearchNewsFromBaidu(search_word):
	if search_word is None or search_word is "":
		return

	driver = webdriver.Firefox(executable_path="geckodriver")
	#driver = webdriver.Chrome()
	driver.maximize_window()
	
	#打开登录页面
	driver.get("http://www.baidu.com") 
	
	#打开超链接 新闻
	news = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')
	news.click()
	
	#获取搜索框
	searchbox = driver.find_element_by_xpath('//*[@id="ww"]')
	
	#填写搜索内容
	searchbox.send_keys(search_word)
	
	#点击搜索按钮
	driver.find_element_by_xpath('//*[@id="s_btn_wr"]').click()

	file=u"百度新闻搜索结果.txt"
	f=codecs.open(file,'w', "GB18030")
	while True:
		#获取新闻标题 在所有的class为mainArea的div里取h3 
		news_titles = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_xpath("//div[@class='result']/h3/a"))
		for news in news_titles:
			print news.text
			f.write(news.text + "\r\n")

		#点击下一页
		try:
			time.sleep(1)
			aname=u'下一页>'
			nextpage = driver.find_element_by_xpath('//a[contains(@class, "n") and contains(text(), "' +aname+ '")]')
			nextpage.click()
		except:
			break
	f.close()

if __name__ == '__main__':
	word=u"北语语言智能与技术"
	if len(sys.argv) > 1:
		word = sys.argv[1].decode("gbk","ignore")

	SearchNewsFromBaidu(word)
