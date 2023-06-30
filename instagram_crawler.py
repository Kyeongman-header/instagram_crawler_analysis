
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
#셀레니움 3.11.0 버전에서.

dr = webdriver.Chrome(executable_path="./chromedriver.exe") #웹드라이버로 크롬 웹 켜기. 
dr.set_window_size(414, 800) 	#브라우저 크기 414*800으로 고정
dr.get('https://www.instagram.com/') #인스타그램 웹 켜기
time.sleep(3) 	#2초 대기
id_box = dr.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input").send_keys('')   #아이디 입력창
password_box = dr.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys( '')    #비밀번호 입력창
login_button = dr.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button').click()  
# login_button = dr.find_element_by_css_selector('#loginForm > div > div:nth-child(4) > button').click()     #로그인 버튼

# #동작 제어
# act = ActionChains(dr)      #동작 명령어 지정

time.sleep(3)
#mount_0_0_F9 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div
# btn_later1 = dr.find_element_by_css_selector('mount_0_0_F9 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div')
# btn_later1.click()
# time.sleep(3)
# # 알림 설정 팝업창 제거 ("나중에 하기 버튼 클릭")
# #mount_0_0_by > div > div > div > div:nth-child(3) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1
# btn_later2 = dr.find_element_by_css_selector('#mount_0_0_by > div > div > div > div:nth-child(3) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1')
# btn_later2.click()
# time.sleep(3)

_keyword = '야구직관' # 검색할 키워드
dr.get('https://www.instagram.com/explore/tags/' + _keyword + '/')

time.sleep(12)
first=dr.find_element_by_css_selector("div:nth-child(1) > div:nth-child(1) > a > div._aagu > div._aagw")
first=first.click()
count=0
import random

from tqdm import tqdm, trange
for window in trange(50000):
    rand_time=random.uniform(0.5,1.5)
    time.sleep(rand_time)
    img=dr.find_elements_by_css_selector('div > div > div > ul > li:nth-child(2) > div > div > div > div > div._aagv > img')
    img_2=dr.find_elements_by_css_selector('div > div > div > div > div._aagu._aa20._aato > div._aagv > img')
    if len(img)>0:
        print(img[0])
        source=img[0].get_attribute('src')
        label=img[0].get_attribute('alt')
        print(label)
    
        try:
            urllib.request.urlretrieve(source,"pictures/test__"+str(count)+".jpg")
            count+=1
        except:
            print("error source.")
            print(source)
            time.sleep(2)
    if len(img_2)>0:
        print(img_2[0])
        source=img_2[0].get_attribute('src')
        label=img_2[0].get_attribute('alt')
        print(label)
        try:
            urllib.request.urlretrieve(source,"pictures/test__"+str(count)+".jpg")
            count+=1
        except:
            print("error source.")
            print(source)
            time.sleep(2)

    inner_next=dr.find_elements_by_class_name('_afxw._al46._al47')
    if len(inner_next)!=0:
        inner_next[0].click()
        continue
    

    next=dr.find_element_by_css_selector("div._aaqg._aaqh > button")
    next=next.click()

    
    
# img=dr.find_elements_by_xpath('//img')
# for i in range(len(img)):
#     source=img[i].get_attribute('src')
#     if source.find('https://scontent-')>=0:
#         try:
#             urllib.request.urlretrieve(source,"pictures/test_"+str(i)+".jpg")
#         except:
#             print("error source.")
#             print(source)
#             continue



# SCROLL_PAUASE_TIME=6
# count=0
# ss=[]
# while True:

#     time.sleep(SCROLL_PAUASE_TIME)

#     #스크롤을 내려준다

#     last_height = dr.execute_script("return document.body.scrollHeight")

#     dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     time.sleep(SCROLL_PAUASE_TIME)

#     new_height = dr.execute_script("return document.body.scrollHeight")
#     img=dr.find_elements_by_xpath('//img')
#     for i in range(len(img)):
#         source=img[i].get_attribute('src')

#         label=img[i].get_attribute('alt')
#         # print(label)
#         # print(source)

#         if source in ss:
#             continue
        
#         ss.append(source)

#         if source.find('https://scontent-')>=0:

#             try:
#                 urllib.request.urlretrieve(source,"pictures/test_"+str(count)+".jpg")
#                 count+=1
#             except:
#                 print("error source.")
#                 print(source)
#                 continue
    
#     print("new updated length.")
#     print(len(ss))
    
    
#     if new_height == last_height:
#         while True:
#             dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#             time.sleep(SCROLL_PAUASE_TIME)

#             new_height = dr.execute_script("return document.body.scrollHeight")

#             if new_height == last_height:
#                 print("스크롤 안 내려감.. 잠시 위로 올렸다 내리기.")
#                 dr.execute_script("window.scrollTo(0, document.body.scrollHeight*0.9);")
#                 time.sleep(SCROLL_PAUASE_TIME)
#                 continue

#             else:

#                 last_height = new_height

#                 break

 
