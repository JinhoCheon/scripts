from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1024,768")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://kream.co.kr/')


def is_page_exist(xpath):
    try:
        elements = driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException as e:
        return False
        

def apply_store(xpath):
    count = 0
    while True:
        
        if is_page_exist(xpath) == False:
            break

        elements = driver.find_element(By.XPATH, xpath)
        elements.click()

        print("[",count,"] 신규 보관 신청이 제한된 카테고리의 상품입니다.")

        count += 1

        time.sleep(random.uniform(8, 9))

       
def pay_store_fee():
    count = 0
    pay1_xpath = '/html/body/div[1]/main/div[2]/div[2]/div/div/div/div/div/div[5]/button/span/em'
    chk1_xpath = '/html/body/div[1]/main/div[2]/div[6]/div/div[2]/div[3]/div[1]/div/div[2]/label/span/svg'
    chk2_xpath = '/html/body/div[1]/main/div[2]/div[6]/div/div[2]/div[3]/div[1]/div/div[3]/label/span/svg'
    chk3_xpath = '/html/body/div[1]/main/div[2]/div[6]/div/div[2]/div[3]/div[1]/div/div[4]/label/span/svg'
    chk4_xpath = '/html/body/div[1]/main/div[2]/div[6]/div/div[2]/div[3]/div[1]/div/div[5]/label/span/svg'
    pay2_xpath = '/html/body/div[1]/main/div[2]/div[6]/div/div[2]/div[4]/div/button/span/em'
    
    while True:
        pay1_btn = driver.find_element(By.Xpath, pay1_xpath)
        pay1_btn.click()
        time.sleep(3)
        
        chk_box1 = driver.find_element(By.Xpath, chk1_xpath)
        chk_box1.click()
        time.sleep(1)
        chk_box2 = driver.find_element(By.Xpath, chk2_xpath)
        chk_box2.click()
        time.sleep(1)
        chk_box3 = driver.find_element(By.Xpath, chk3_xpath)
        chk_box3.click()
        time.sleep(1)
        chk_box4 = driver.find_element(By.Xpath, chk4_xpath)
        chk_box4.click()
        time.sleep(1)
        pay2_btn = driver.find_element(By.Xpath, pay2_xpath)
        pay2_btn.click()
        time.sleep(3)

        if is_page_exist(pay1_xpath) == False:
            break

        print("[",count,"] 신규 보관 신청이 제한된 카테고리의 상품입니다.")
        count += 1


def main():
    apply_xpath = '//*[@id="__nuxt"]/main/div[2]/div[3]/div/div/div/div/div[4]/a'

    while True:
        result = is_page_exist(apply_xpath)
        if result == True:
            break
        time.sleep(10)
    
    apply_store(apply_xpath)
    time.sleep(10)
    pay_store_fee()

if __name__ == "__main__":
    main()