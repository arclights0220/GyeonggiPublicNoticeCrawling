from asyncio import sleep
from asyncio.windows_events import NULL
from datetime import date, datetime
from ntpath import join
from posixpath import split, splitext
from socket import TCP_NODELAY
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import html.parser
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
import warnings
from selenium.webdriver.common.keys import Keys
import webbrowser
import os
warnings.filterwarnings(action='ignore')



chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
    0]  # 크롬드라이버 버전 확인
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
# 크롬드라이버 업데이트
try:
    driver = webdriver.Chrome(
        f'./{chrome_ver}/chromedriver.exe', chrome_options=options)
except:
    chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome(
        f'./{chrome_ver}/chromedriver.exe', chrome_options=options)




driver.execute_script("window.onbeforeunload = function() {};")

def gapyeong(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.gp.go.kr/portal/selectGosiList.do?key=2148&not_ancmt_se_code=01"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div[2]/div/div[1]/form/fieldset/input[3]')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/div[2]/div/div[1]/form/fieldset/input[4]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#board > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n가평군청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:6]
            print("\n가평군청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n가평군청 사이트 오류") 
        print("\n" + url)
        webbrowser.open(url)
        pass


def goyang(a):
    try:
        driver.implicitly_wait(15)
        url = "http://www.goyang.go.kr/www/link/BD_notice.do"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[3]/article/div[3]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            "/html/body/form/div[1]/fieldset/div/div/input")
        btn = driver.find_element_by_xpath(
            '/html/body/form/div[1]/fieldset/div/div/span/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div.table-responsible > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n고양시청 고시공고 "+ a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n고양시청 고시공고 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n고양시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)

def goyang2(a):
    try:
        driver.implicitly_wait(15)
        url = "http://www.goyang.go.kr/www/link/BD_bidding.do"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[3]/article/div[3]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            "/html/body/form/div[1]/fieldset/div/div/input")
        btn = driver.find_element_by_xpath(
            '/html/body/form/div[1]/fieldset/div/div/span/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div.table-responsible > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n고양시청 입찰공고 "+ a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n고양시청 입찰공고 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n고양시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)


def gccity(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.gccity.go.kr/portal/saeol/gosi/list.do?mId=0301040000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[6]/section[2]/div[1]/form/div[1]/fieldset/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[6]/section[2]/div[1]/form/div[1]/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n과천시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n과천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n과천시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass

def gm(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.gm.go.kr/pt/user/nftcBbs/BD_selectNftcBbsList.do?q_nftcBbsCode=1001"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[3]/form/div[1]/div/input[3]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[3]/form/div[1]/div/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#c-contents > div.sub_content_cont_rt_cont > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n광명시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n광명시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n광명시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass

def gjcity(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.gjcity.go.kr/portal/saeol/gosi/list.do?mId=0202010000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section[2]/div[1]/form/div[2]/fieldset/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section[2]/div[1]/form/div[2]/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n광주시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n광주시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n광주시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass


def guri(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.guri.go.kr/cms/content/view/1676"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[2]/div[2]/p/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            "/html/body/form/div/fieldset/div/input[1]")
        btn = driver.find_element_by_xpath(
            '/html/body/form/div/fieldset/div/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n구리시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-1:]
            print("\n구리시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n구리시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass


def gunpo(a):
    try:
        driver.implicitly_wait(15)
        url = "http://www.gunpo.go.kr/www/contents.do?key=3907"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div/div/div/main/article/div/iframe")
        driver.switch_to.frame(iframe)

        box = driver.find_element_by_xpath(
            "/html/body/form/table[2]/tbody/tr[2]/td[2]/input")
        btn = driver.find_element_by_xpath(
            '/html/body/form/table[2]/tbody/tr[2]/td[2]/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(22) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(5)')
        if not search_result:
            print("\n군포시청 에러")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-1:]
            print("\n군포시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n군포시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def gimpo(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.gimpo.go.kr/portal/ntfcPblancList.do?key=1004&cate_cd=1&searchCnd=40900000000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div/main/article/div/div/div[1]/form/fieldset/input[2]')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div/main/article/div/div/div[1]/form/fieldset/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n김포시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n김포시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n김포시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def nyj(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.nyj.go.kr/main/185?space=main_board_gonggo"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[6]/form/fieldset/p/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[6]/form/fieldset/p/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > article > div.modules_board > div > div.list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n남양주시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-1:]
            print("\n남양주시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n남양주시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def ddc(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.ddc.go.kr/ddc/selectGosiList.do?key=107&not_ancmt_se_code=01"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/article/div[3]/div[1]/form/span/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/article/div[3]/div[1]/form/span/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n동두천시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n동두천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n동두천시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass



def bucheon(a):
    try:
        driver.implicitly_wait(15)
        url = "http://www.bucheon.go.kr/site/homepage/menu/viewMenu?menuid=148002003001"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div[2]/div[2]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            "/html/body/form/div[1]/fieldset/div[2]/input[1]")
        box.send_keys(a)
        box.send_keys(Keys.ENTER)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div.default_board > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n부천시청 에러")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n부천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n부천시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def seongnam(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.seongnam.go.kr/notice/publicNotice.do?menuIdx=1000499&returnURL=%2Fmain.do"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath('/html/body/form/div[4]/p/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/div[4]/p/span/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#form1 > div.tblWrap > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n성남시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n성남시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n성남시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass


def suwon(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.suwon.go.kr/sw-www/www04/www04-06.jsp"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/main/article/div/div[1]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            '/html/body/form/div/div/div[1]/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/div/div/div[1]/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n수원시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n수원시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n수원시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def siheung(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.siheung.go.kr/main/saeol/gosi/list.do?mId=0401040000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/section[2]/div[1]/form/div[2]/fieldset/ul/li[2]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/section[2]/div[1]/form/div[2]/fieldset/ul/li[3]/input')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n시흥시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n시흥시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n시흥시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def ansan(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www2.ansan.go.kr/www/common/cntnts/selectContents.do?cntnts_id=C0001209"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div/main/article/div/div/div/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            '/html/body/form/div/fieldset[1]/div/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/div/fieldset[1]/div/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div > fieldset:nth-child(4) > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n안산시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n안산시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n안산시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass

def anseong(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.anseong.go.kr/portal/saeol/gosiList.do?mId=0401040000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[5]/div/div[2]/form/div[1]/div[1]/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[5]/div/div[2]/form/div[1]/div[1]/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#listForm > div.gosi_wrap > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n안성시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:3]
            print("\n안성시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n안성시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def anyang(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.anyang.go.kr/main/selectEminwonList.do?key=263&notAncmtSeCode=01,04&ofr_pageSize=10"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/main/article/div/div/form/fieldset/div/div/input[2]')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/main/article/div/div/form/fieldset/div/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n안양시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:3]
            del splittext[-1:]
            print("\n안양시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n안양시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def yangju(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.yangju.go.kr/www/contents.do?key=211"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/main/article/div/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr/td[3]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr/td[5]/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#list2 > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n양주시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n양주시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n양주시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def yp(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.yp21.go.kr/www/selectBbsNttList.do?bbsNo=5&key=1119"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/fieldset/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/fieldset/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n양평시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-4:]
            print("\n양평시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n양평시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def yeoju(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.yeoju.go.kr/www/jsp/project/gosi/list.jsp"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div[2]/form/input[4]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div[2]/form/input[5]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content_box > div.board_wrap_bbs.boardTop_txt > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n여주시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n여주시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n여주시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def yeoncheon(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.yeoncheon.go.kr/www/selectGosiList.do?key=3393&not_ancmt_se_code=01"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/article/div/div/div[1]/form/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/main/article/div/div/div[1]/form/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n연천시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n연천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext) + "\n\n")
    except:
        print("\n연천시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def osan(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.osan.go.kr/portal/saeol/gosi/list.do?mId=0302010000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/fieldset/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n오산시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n오산시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n오산시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def yongin(a):
    try:
        driver.implicitly_wait(15)
        url = "http://www.yongin.go.kr/user/bbs/BD_selectBbsList.do?q_bbsCode=1004&q_clCode=5"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[3]/div[2]/form/div[1]/div/input[4]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[3]/div[2]/form/div[1]/div/button[1]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div.cont_box > div.t_list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n용인시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            print("\n용인시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n용인시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass               


def uiwang(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.uiwang.go.kr/UWKORINFO0701"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div/main/div/section/div[2]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            '/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td[3]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td[4]/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(23) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6)')
        if not search_result:
            print("\n의왕시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n의왕시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n의왕시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def ui4u(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.ui4u.go.kr/portal/saeol/gosiList.do?seCode=01&mId=0301040000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/section[2]/div[1]/form/div[1]/fieldset/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/section[2]/div[1]/form/div[1]/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#listForm > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n의정부시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n의정부시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n의정부시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def icheon(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.icheon.go.kr/portal/selectNoticeWebList.do?key=1606&searchNotAncmtSeCd=01"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/main/article/div/div/form/fieldset/div/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/main/article/div/div/form/fieldset/div/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n이천시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            print("\n이천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n이천시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def paju(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.paju.go.kr/user/board/BD_board.list.do?bbsCd=1022&q_ctgCd=4063"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[1]/div/article/div[3]/div/form/div[1]/div/fieldset/div/div/div[2]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[1]/div/article/div[3]/div/form/div[1]/div/fieldset/div/div/div[3]/div/button[1]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#dataForm > div.table.table-list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n파주시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-4:]
            print("\n파주시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n파주시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def puc(a): 
    try:
        driver.implicitly_wait(15)
        url = "https://www.puc.or.kr/noticeInfo/noticeInfoList.do"
        driver.get(url)
        btn2 = driver.find_element_by_xpath(
            '/html/body/div/form[4]/main/section/div[1]/div/ol/li[3]/div/div/a[3]')
        btn3 = driver.find_element_by_xpath('//*[@id="dropdownMenuButton"]')
        btn3.click()
        btn2.click()
        box = driver.find_element_by_id('searchstring')
        btn = driver.find_element_by_xpath(
            '/html/body/div/form[4]/main/section/div[2]/div[2]/div/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > section > div.section-content > div.table-wrap > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n평택도시공사 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-1:]
            print("\n평택도시공사 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n평택도시공사 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def pyeongtaek(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.pyeongtaek.go.kr/pyeongtaek/saeol/gosiList.do?seCode=01&mId=0401020000"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[4]/div/section[2]/div[2]/form/div[1]/div[2]/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[4]/div/section[2]/div[2]/form/div[1]/div[2]/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#listForm > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n평택시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n평택시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n평택시청 사이트 오류")
        webbrowser.open(url) 
        print("\n" + url)
        pass

def pocheon(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.pocheon.go.kr/www/contents.do?key=5175&"
        driver.get(url)
        iframe = driver.find_element_by_id(
            "iframeaction")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath(
            '/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td[3]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td[4]/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(23) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6)')
        if not search_result:
            print("\n포천시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n포천시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n포천시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)


def hanam(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.hanam.go.kr/www/selectGosiList.do?key=171&not_ancmt_se_code=01,03,04"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div/div/div/main/article/div/form/div/div/div[2]/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div/main/article/div/form/div/div/div[2]/div/span[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n하남시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n하남시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n하남시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

def hscity(a):
    try:
        driver.implicitly_wait(15)
        url = "https://www.hscity.go.kr/www/link/BD_notice.do"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[2]/div[3]/iframe')
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath('/html/body/div/form/div/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div/form/div/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contentDiv > form > table.boardDefalut > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n화성시청 " + a + "에 관한 최신공고 : ")
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n화성시청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                for _ in splittext))
    except:
        print("\n화성시청 사이트 오류") 
        webbrowser.open(url)
        print("\n" + url)
        pass

what = input("\n검색할 문장 혹은 단어를 입력하세요 : ")

allprocess = [gapyeong(what),
              goyang(what),
              goyang2(what),
              gccity(what),
              gjcity(what),
              gm(what),
              gunpo(what),
              guri(what),
              gimpo(what),
              nyj(what),
              bucheon(what),
              seongnam(what),
              suwon(what),
              siheung(what),
              ansan(what),
              anseong(what),
              anyang(what),
              yp(what),
              yeoju(what),
              osan(what),
              yongin(what),
              uiwang(what),
              ui4u(what),
              icheon(what),
              pyeongtaek(what),
              puc(what),
              hanam(what),
              hscity(what),
              ddc(what),
              paju(what),
              pocheon(what),
              yeoncheon(what),
              yangju(what)]

for i in allprocess:
    i
    driver.delete_all_cookies()
