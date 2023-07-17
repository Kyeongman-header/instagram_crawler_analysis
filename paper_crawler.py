
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import urllib.parse
import urllib.request
import time
import datetime
import csv

dr = webdriver.Chrome(executable_path="./chromedriver.exe") #웹드라이버로 크롬 웹 켜기. 
dr.set_window_size(1500, 2000) 	#브라우저 크기 414*800으로 고정
dr.get('https://www.dbpia.co.kr/journal/publicationDetail?publicationId=PLCT00007284#none') #인스타그램 웹 켜기
time.sleep(2) 	#2초 대기
#sidebarPub
#searchListArea > li > div.listBox > div.titWrap > h5 > a
#//*[@id="searchListArea"]/li/div[1]/div[1]
# //*[@id="searchListArea"]/li/div[1]/div[1]
#searchListArea > li > div.listBox > div.img
#sidebarPub
lists=dr.find_elements_by_css_selector('#sidebarPub')

lists[0].click()
lists[0].click()

def abstract_and_keywords(dr):
    try:
        title=dr.find_elements_by_css_selector('#thesisTitle')
        print(title[0].text)

        abstract=dr.find_elements_by_css_selector(' div.abstractTxt')
        # print(abstract)
        abstract=abstract[0].text
        print(abstract)
        
        i=1
        while True:
            
            keyword=dr.find_elements_by_css_selector(' div.keywordWrap > a:nth-child('+str(i)+')')
            if len(keyword)==0:
                break
            print(keyword[0].text)

            i +=1
    except:
        print("no var")
now_page=0
while True:
    for i in range(1,7):
        paper=dr.find_elements_by_css_selector('#dev_category > li:nth-child('+ str(i) +') > a')
        if len(paper)!=0:
            # try:
                if i>=3:
                    paper[now_page-1].click()
                else:
                    paper[now_page].click()
                #voisNodeList > article:nth-child(2) > article > a > h2
                link=dr.find_elements_by_css_selector('article > a')
                # print(link)
                for k in range(1,20):
                    try:
                        link[k].click()
                        dr.switch_to.window(dr.window_handles[-1])  #새로 연 탭으로 이동
                        
                        
                        abstract_and_keywords(dr)
                        time.sleep(2)
                        dr.close()
                        dr.switch_to.window(dr.window_handles[-1])
                        time.sleep(2)
                    except:
                        continue
                    
            # except:
            #     break
        time.sleep(2)

    
    time.sleep(1)
    lists=dr.find_elements_by_css_selector('#sidebarPub')
    
    # print(lists)
    now_page +=1
    dr.move_to_element(lists[now_page])
    lists[now_page].send_keys(Keys.ENTER)
    time.sleep(2)

