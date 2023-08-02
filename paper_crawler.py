
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



whole_pages=26



dr = webdriver.Chrome(executable_path="./chromedriver.exe") #웹드라이버로 크롬 웹 켜기. 
dr.set_window_size(1500, 2000) 	#브라우저 크기 414*800으로 고정
dr.get('https://www.dbpia.co.kr/journal/publicationDetail?publicationId=PLCT00007284#none') #dbpia 웹
time.sleep(2) 	#2초 대기
#sidebarPub
#searchListArea > li > div.listBox > div.titWrap > h5 > a
#//*[@id="searchListArea"]/li/div[1]/div[1]
# //*[@id="searchListArea"]/li/div[1]/div[1]
#searchListArea > li > div.listBox > div.img
#sidebarPub
lists=dr.find_elements_by_css_selector('#sidebarPub')

lists[0].click()
# ---
lists[0].click()
# ---

twothousand_nine=14
twothousand=23

if whole_pages-26>0:
    new_page=whole_pages-26
    twothousand_nine+=new_page
    twothousand+=new_page


now_page=0
# ---> # n 년도부터 수집하기
# dr.execute_script('window.scrollTo(0, 1000);')
# time.sleep(1)
# lists[now_page].click()
# --->

f = open("papers.csv", "w",newline='',encoding='cp949')
writer = csv.writer(f,delimiter=',')
writer.writerow(['title','authors','years','abstract','keywords'])
whole_index=0

def abstract_and_keywords(dr,whole_index):
    #dpMain > section > section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child(1) > span:nth-child(1)
    #dpMain > section > section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child(2) > span:nth-child(1)
    #dpMain > section > section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child(3) > span:nth-child(1)
    #dpMain > section > section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child(1) > span:nth-child(1)
    #dpMain > section > section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child(1) > a
    whole_keywords=[]
    whole_authors=[]
    try:
        
        for i in range(1,6):
            author=dr.find_elements_by_css_selector('section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child('+str(i) +') > span:nth-child(1)')
            
            if len(author)==0:
                author=dr.find_elements_by_css_selector('section.thesisDetail__info > section.thesisDetail__author > ul > li:nth-child('+str(i) +') > a')
                if len(author)==0:
                    break
            
            whole_authors.append(author[0].text)
        
        

        #dpMain > section > section.thesisDetail__info > section.thesisDetail__journal > ul > li:nth-child(4) > span:nth-child(1)
        years=dr.find_elements_by_css_selector('section.thesisDetail__info > section.thesisDetail__journal > ul > li:nth-child(4) > span:nth-child(1)')
        # print(years[0].text)
        years_words=years[0].text

        title=dr.find_elements_by_css_selector('#thesisTitle')
        # print(title[0].text)

        title_words=title[0].text
        #dpMain > section > section.thesisDetail__abstract > div
        abstract=dr.find_elements_by_css_selector(' div.abstractTxt')
        
        if len(abstract)==0:
            abstract=dr.find_elements_by_css_selector('section > section.thesisDetail__abstract > div')
        if len(abstract)==0:
            abstract_words="no abstract words"
        else:
            abstract_words=abstract[0].text
        # print(abstract_words)
        
        i=1
        while True:
            
            keyword=dr.find_elements_by_css_selector(' div.keywordWrap > a:nth-child('+str(i)+')')
            if len(keyword)==0:
                break
            # print(keyword[0].text)

            whole_keywords.append(keyword[0].text)
            
            i +=1
        
        # print(whole_keywords)

        whole_keywords = ' '.join(whole_keywords)
        whole_index += 1
        whole_authors=','.join(whole_authors)
        print("index : ")
        print(whole_index)
        print("title and years : ")
        print(title_words + ' ' + years_words)
        print("authors :")
        print(whole_authors)
        # print(abstract_words)
        # print(whole_keywords)


        writer.writerow([title_words,whole_authors,years_words,abstract_words,whole_keywords])

    except Exception as e :
        print(e)
    return whole_index
    
    

# ---
# first = True
# ---
first=False
while True:

    for i in range(1,7): # 2009년부터는 1~4호까지만 있다(그 이후에는 1~6호까지 있으므로, 2023~2009년을 수집하려면 range(1,7)로 바꾼다.)
        if first and i>3:
            first=False
            break
        if now_page>=twothousand_nine and i>4:
            break
        #dev_category > li:nth-child(2)
        #dev_category > li:nth-child(1)
        paper=dr.find_elements_by_css_selector('#dev_category > li:nth-child('+ str(i) +') > a')
        print("paper")
        print(i)
        # print(paper)
        print(len(paper))

        #dev_category > li:nth-child(2)
        #dev_category > li:nth-child(1)
        #dev_category > li:nth-child(1)
        #dev_category > li:nth-child(3)
        #dev_category > li > a
        #dev_category > li:nth-child(1)
        #dev_category > li:nth-child(2)
        #dev_category > li
        #dev_category > li:nth-child(2)
        
        if len(paper)!=0:
            # try:
                actions = ActionChains(dr)
                try:
                    if i>3 or (now_page>=twothousand and i>=2): # 2001년인가에 1호만 있었던 적이 있어서, 그 이후 2호 이상들은 다 now_page -1 을 해야 정상적인 인덱스가 된다...
                            actions.move_to_element(paper[now_page-1])
                            actions.perform()
                            time.sleep(0.5)
                            # actions.send_keys(Keys.PAGE_UP)
                            dr.execute_script('window.scrollTo(0, -250);')
                            time.sleep(0.5)
                            actions.click(paper[now_page-1])
                            actions.perform()
                        

                        # paper[now_page-1].click()
                    else:
                            actions.move_to_element(paper[now_page])
                            actions.perform()
                            time.sleep(1)
                            
                            if now_page<23:
                                dr.execute_script('window.scrollTo(0, -250);')
                            elif now_page>=23 and i>1:
                                lists[now_page].click()
                            
                            time.sleep(1)    
                            actions.click(paper[now_page])
                            actions.perform()
                except Exception as e :
                    print(e)
                    break


                time.sleep(1.5)
                #voisNodeList > article:nth-child(2) > article > a > h2
                link=dr.find_elements_by_css_selector('article > a')
                
                for k in range(1,20):
                    try:
                        link[k].click()
                        dr.switch_to.window(dr.window_handles[-1])  #새로 연 탭으로 이동
                        
                        
                        whole_index=abstract_and_keywords(dr,whole_index)
                        time.sleep(2)
                        dr.close()
                        dr.switch_to.window(dr.window_handles[-1])
                        time.sleep(2)
                    except:
                        continue
                    
            # except:
            #     break
        else:
             break
        time.sleep(2)

    actions = ActionChains(dr)
    time.sleep(1)
    lists=dr.find_elements_by_css_selector('#sidebarPub')
    now_page +=1
    try:
        actions.move_to_element(lists[now_page])
        actions.perform()
        # actions.send_keys(Keys.PAGE_UP)
        dr.execute_script('window.scrollTo(0, -250);')
        actions.click(lists[now_page])
        actions.perform()
        
    except:
        continue
    time.sleep(2)

