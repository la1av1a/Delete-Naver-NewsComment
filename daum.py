import os
import sys

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main(id, pw):
    def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        return driver

    def kakao_Login():
        URL = "https://news.v.daum.net/v/20220524110001438"
        driver.get(URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="btnMinidaumLogin"]'))
        ).click()
        driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/div/div/div[2]/a').click()
        driver.find_element(By.XPATH, '//*[@id="id_email_2"]').send_keys(id)
        driver.find_element(By.CSS_SELECTOR, '#id_password_3').send_keys(pw)
        driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="alex-area"]/div/div/div/div[1]/button/span'))
        ).click()
        driver.find_element(By.XPATH, '//*[@id="alex-area"]/div/div/div/div[1]/a/span').click()

    def delete_comment():
        driver.implicitly_wait(10)
        ele = driver.find_element(By.CSS_SELECTOR,
                                  '#alex-area > div > div > div:nth-child(2) > div.my_layer.my_layer_type2.use_unfollow > div.my_header > div > div > ul > li.on > a > span > span[data-reactid=".0.0.1.1.0.1.1.0.$mycmt_tab_comment.0.0.3"]')
        amountOfComments = ele.text
        print(f'총 댓글 갯수 : {amountOfComments}')
        while int(amountOfComments) > 0:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#alex-area > div > div > div:nth-child(2) > div.my_layer.my_layer_type2.use_unfollow > div.my_header > div > div > ul > li.on > a > span > span[data-reactid=".0.0.1.1.0.1.1.0.$mycmt_tab_comment.0.0.3"]'))
            )
            element.click()
            ele = driver.find_element(By.CSS_SELECTOR,'#alex-area > div > div > div:nth-child(2) > div.my_layer.my_layer_type2.use_unfollow > div.my_header > div > div > ul > li.on > a > span > span[data-reactid=".0.0.1.1.0.1.1.0.$mycmt_tab_comment.0.0.3"]')
            # ele = driver.find_element(By.CSS_SELECTOR,'#alex-area > div > div > div:nth-child(2) > div.my_layer.my_layer_type2.use_unfollow > div.my_header > div > div > ul > li.on > a > span > span[data-reactid=".0.0.1.1.0.1.1.0.$mycmt_tab_comment.0.0.3"]')
            s = driver.find_element(By.XPATH, '//*[contains(@class, "inner_layer")]/div/ul/li[1]/div/button')
            s.click()
            driver.find_element(By.CLASS_NAME, 'link_delete').click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            print(f'남은 댓글 갯수 : {ele.text}개')
    try:
        driver = set_chrome_driver()
        kakao_Login()
        delete_comment()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])