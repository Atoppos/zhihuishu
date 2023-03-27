import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
import qrcode
from pyzbar.pyzbar import decode
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_img():
    src=driver.find_element(By.XPATH,"//div[@class='code-border']/img").get_attribute('src')
    image_encoded=src.replace('data:image/png;base64,','')
    body=base64.b64decode(image_encoded)
    file=open('pic.jpg','wb')
    file.write(body)
    file.close()
    barcodes=decode(Image.open('pic.jpg'))
    for barcode in barcodes:
        barcode_url=barcode.data.decode('utf-8')
    qr=qrcode.QRCode(
        version=5,
        border=1
    )
    qr.add_data(barcode_url)
    qr.print_ascii(invert=True)
    print('请扫码登录')
    os.remove('pic.jpg')

def log_in():
    load_img()
    try:
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.CLASS_NAME, 'success-box')))
    except:
        js="document.getElementsByClassName('shadow')[0].style.display='block';"
        driver.execute_script(js)
        driver.find_element(By.CLASS_NAME,'refresh').click()
        time.sleep(2)
        print('验证码超时，请重新扫码')
        log_in()
        
    else:
        print('扫码成功')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'headerMain')))
    except:
        js="document.getElementsByClassName('shadow')[0].style.display='block';"
        driver.execute_script(js)
        driver.find_element(By.CLASS_NAME,'refresh').click()
        time.sleep(2)
        print('登录失败,请重新扫码')
        log_in()
    else:
        print('登陆成功')
        print('已进入主页面')

def find_class():
    href=driver.find_element(By.XPATH,'//ul[@class="header-menu__wrap"]/li[4]/a').get_attribute('href')
    driver.get(href)
    print('已进入课程界面')
    try:
        driver.find_element(By.XPATH,"//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]").click()
    except:
        print('无弹窗')
    class_list=[]
    class_li=driver.find_elements(By.CLASS_NAME,'courseName')
    for i in class_li:
        class_list.append(i.text)
    no=1
    for i in class_list:
        print('%d:%s'%(no,i))
        no+=1
    select=int(input('请输入课程编号：'))
    selection=int(select)
    class_name=driver.find_element(By.XPATH,"//div[@id='sharingClassed']/div[2]/ul[%d]/div/dl/dd/div/img"%(selection))
    ActionChains(driver).move_to_element(class_name).click().perform()

def skip_class():
    try:
        driver.find_element(By.XPATH,'//div[@id="app"]/div[1]/div[6]/div[2]/div[1]/i').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//div[@id="app"]/div[1]/div[6]/div[1]/div[3]/span/button').click()
        time.sleep(1)
    except:
        print('播放页面无弹窗')

    try:
        driver.find_element(By.XPATH,'//ul[@class="topic-list"]/li[1]').click()
    except:
        print('播放页面无答题窗口')
    finally:
        time.sleep(1)

    try:
        driver.find_element(By.XPATH,'//div[@class="btn"]').click()
    except:
        pass
    finally:
        time.sleep(1)
    is_end()
    time.sleep(2)
    contro=driver.find_element(By.XPATH,"//div[@id='container']")
    ActionChains(driver).move_to_element(contro).click().perform()
    print('已开始播放')
    ActionChains(driver).move_to_element(contro).click(driver.find_element(By.XPATH,"//div[@class='volumeIcon']")).perform()
    print('已静音')

def answer():
        try:
            driver.find_element(By.XPATH,'//ul[@class="topic-list"]/li[1]').click()
            driver.find_element(By.XPATH,'//div[@class="btn"]').click()
            print('出现答题弹窗')
            time.sleep(2)
            contro=driver.find_element(By.XPATH,"//div[@id='container']")
            ActionChains(driver).move_to_element(contro).click().perform()
        except:
            print('未出现答题弹窗')

def duration():
        try:
            contro=driver.find_element(By.XPATH,"//div[@id='container']")
            ActionChains(driver).move_to_element(contro).perform()
            current_time=driver.find_element(By.XPATH,'//div[@class="nPlayTime"]/span[1]').text
            duration_time=driver.find_element(By.XPATH,'//div[@class="nPlayTime"]/span[2]').text
            print('当前时长为:{},总时长为:{}'.format(str(current_time),str(duration_time)))
        except:
            pass

def is_end():
        try:
            contro=driver.find_element(By.XPATH,"//div[@id='container']")
            ActionChains(driver).move_to_element(contro).perform()
            current_time=driver.find_element(By.XPATH,'//div[@class="nPlayTime"]/span[1]').text
            duration_time=driver.find_element(By.XPATH,'//div[@class="nPlayTime"]/span[2]').text
            if(current_time==duration_time):
                contro=driver.find_element(By.XPATH,"//div[@id='container']")
                ActionChains(driver).move_to_element(contro).click(driver.find_element(By.XPATH,'//div[@id="nextBtn"]')).perform()
                return True
        except:
            pass

def class_end():
        try:
            driver.find_element(By.XPATH,"//div[@id='app']/div[1]/div[7]/div/div[1]/button").click()
            return True
        except:
            pass
        
if __name__=='__main__':
    print('是否清理进程')
    print('1:是    2:否')
    a=int(input('请输入：'))
    if(a==1):
        try:
            os.system('taskkill /im chromedriver.exe /F')
            os.system('taskkill /im chrome.exe /F')
        except:
            pass
        else:
            print('已清理进程')
    input('按回车开始进程')
    option = webdriver.ChromeOptions()
    option.add_argument('-ignore-certificate-errors')
    option.add_argument('-ignore -ssl-errors')
    option.add_argument('---ignore-certificate-errors-spki-list')
    option.add_argument('--ignore-ssl-error')
    option.add_argument('log-level=2')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('disable-infobars')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitcher', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=option,options=options,executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get('https://passport.zhihuishu.com/login#qrCodeLogin')
    driver.implicitly_wait(10)
    log_in()
    find_class()
    while(True):
        skip_class()
        print('开始刷课')
        while(True):
            answer()
            duration()
            over=class_end()
            if(over==True):
                break
            if(is_end()==True):
                print('已播完当前章节,即将开始下一章节')
                break
            time.sleep(20)
        if(over==True):
            break
    print('今日已刷完')
    input('请按回车退出')
    driver.quit()