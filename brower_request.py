"""this file is visit by selenium"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.alert import Alert
import selenium.common.exceptions as exceptionC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver import ActionChains
from Qingmu import Subway,Newsuper_r



ck_list=[]

class Browser_login():
    def __init__(self,sdate,edate):
        self.options=webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches",['enable-automation'])  #关闭自动测试状态
        self.options.add_experimental_option('useAutomationExtension', False) #禁用自动化拓展
        self.options.add_experimental_option('detach',True) #保持运行之后不会自动关闭
        self.options.add_argument('--lang=zh-CN')

        # self.remote_debugging_port = random.randint(9222, 9999)
        # self.user_data_dir=r'E:\python_file\非自用工具箱\SeleniumUserData'
        # self.options.add_experimental_option('debuggerAddress', f'''127.0.0.1:{self.remote_debugging_port}''')
        # subprocess.Popen([
        #     r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        #     f'''--remote-debugging-port={self.remote_debugging_port}''',
        #     f'''--user-data-dir={self.user_data_dir}'''], True)

        self.browser = webdriver.Chrome(options=self.options) #不同浏览器调用的类不同，如Edge、Safari、Firefox等等
        self.wait = WebDriverWait(self.browser, 30,0.5)
        self.sdate=sdate
        self.edate=edate
        self.cookdir={}

    def login(self,username,password):
        alimama_url = 'https://www.alimama.com/member/login.htm'
        self.browser.get(alimama_url)
        self.browser.implicitly_wait(4)
        frame_sign = self.browser.find_element(By.XPATH,
                                          '//*[contains(@src,"https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true&disableQuickLogin=true")]')
        self.browser.switch_to.frame(frame_sign)
        # print(browser.page_source)
        input_user = self.browser.find_element(By.ID, 'fm-login-id')
        input_password = self.browser.find_element(By.ID, 'fm-login-password')
        confirm_sign = self.browser.find_element(By.CSS_SELECTOR, '.fm-button.fm-submit.password-login')
        script_navigatorchange = 'Object.defineProperties(navigator,{webdriver:{get:()=> false,}})'
        input_user.send_keys(username)
        input_password.send_keys(password)
        self.browser.execute_script(script_navigatorchange)
        time.sleep(2)
        confirm_sign.click()
        self.browser.implicitly_wait(7)
        try:
            time.sleep(4)
            self.wait.until(Ec.presence_of_element_located((By.XPATH, "//*[@data-spm='13868764']")))
        except Exception:
            time.sleep(30)
            self.wait.until(Ec.presence_of_element_located((By.XPATH, "//*[@data-spm='13868764']")))

        self.cookieget()
        time.sleep(1)
        self.browser.quit()
        # self.browser.quit()
        # print("ce:",self.browser.get_cookies())

    def cookies_format(self,url):
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        time.sleep(4)
        cookie_init =self.browser.get_cookies()
        self.browser.implicitly_wait(10)
        cookies=""
        for cookiei in cookie_init:
            cookief = '{0}={1},'
            cookief = cookief.format(cookiei.get('name'), cookiei.get('value'))
            cookies+=cookief
        time.sleep(1)
        # print(cookies)
        return cookies

    def cookieget(self):
        subway_url="https://subway.simba.taobao.com/#!/home/index-new"
        newsuper_url='https://tuijian.taobao.com/indexbp-display.html'
        aipush_url='https://adbrain.taobao.com/indexbp.html'
        taoke_url='https://ad.alimama.com/dashboard.htm'
        self.cookdir['subway_cook']=self.cookies_format(subway_url)
        self.cookdir['newsuper_cook']=self.cookies_format(newsuper_url)
        self.cookdir['aipush_cook']=self.cookies_format(aipush_url)
        self.cookdir['taoke_cook']=self.cookies_format(taoke_url)


    def subway_download(self):
        # try:
        Subway(2,self.sdate,self.edate).download_subway(self.cookdir["subway_cook"])
        # except Exception as sub_error:
        #     print("请检查登录状态！")
        #     print("error: \n",sub_error)

    def newsuper_download(self):
        # try:
        Newsuper_r(2).download_newsuper(self.cookdir["newsuper_cook"])
        # except Exception as sub_error:
        #     print("请检查登录状态！")
        #     print("error: \n",sub_error)





if __name__ == "__main__":
    sdate="2022-01-01"
    edate="2022-01-28"
    target=Browser_login(sdate,edate)
    target.login("skechers官方旗舰店:推广01","SKXNV0102")
    # target.newsuper_download()
    # target.subway_download()