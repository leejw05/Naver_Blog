from argparse import Action
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

from Infos import data as info

class Posting:
    driver = webdriver.Chrome(executable_path='./chromedriver')
    actions = ActionChains(driver)
    
    def __init__(self,Items):
        self.Items = Items
        URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
        self.driver.get(url=URL)
        
    def Login(self,userID,userPWD):
        ID = self.driver.find_element_by_css_selector(".input_text[name='id']")
        PASSWORD = self.driver.find_element_by_css_selector(".input_text[name='pw']")
        
        pyperclip.copy(userID)
        time.sleep(0.5)
        ID.send_keys(Keys.COMMAND , "v")
        time.sleep(0.5)
        pyperclip.copy(userPWD)
        time.sleep(0.5)
        PASSWORD.send_keys(Keys.COMMAND , "v")

        submit = self.driver.find_element_by_class_name("btn_login")
        submit.click()
        time.sleep(2)
        pass

    
    def moveWritePage(self):
        self.driver.get("https://blog.naver.com/PostWriteForm.naver?blogId=dlwjddn3130&Redirect=Write&redirect=Write&widgetTypeCall=true&topReferer=https%3A%2F%2Fnid.naver.com%2F&directAccess=false")
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1)
        return
        
    def WriteArticle(self ,Title,Article):
        self.moveWritePage()

        self.SubmitButton()
        time.sleep(1)
        self.actions.send_keys(Title).perform()
        time.sleep(0.3)
        self.SubmitButton() #제목을 적지않고 발행해서 제목칸으로 커서를 옮김
        time.sleep(0.5)
        self.actions.send_keys(Article).perform()
        self.SubmitButton()
        pass

    def SubmitButton(self): #발행 버튼 클릭
        self.driver.find_element_by_css_selector(".publish_btn__Y5mLP").click() #발행 펼치는 버튼 클릭
        time.sleep(0.3)
        self.driver.find_element_by_css_selector(".confirm_btn__Dv9du").click() #발행버튼
        


Items = [
    {
        'Title' : "제목 1",
        'Article' : "제목1의 글입니다"
    },
    {
        'Title' : "제목 2",
        'Article' : "제목2의 글입니다"
    },
    {
        'Title' : "제목 3",
        'Article' : "제목1의 글입니다"
    }
]


posting = Posting(Items)

posting.Login(info.ID,info.PWD)

for item in Items:
    posting.WriteArticle(item['Title'],item['Article'])
    time.sleep(10)