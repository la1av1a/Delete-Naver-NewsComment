import os
import sys

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


id = sys.argv[1]
pw = sys.argv[2]

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()
URL = "https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fn.news.naver.com%2Farticle%2Fcomment%2F346%2F0000050936" \
      "&svctype=0 "



def main():
    try:
        driver.get(URL)
        _login(driver, id, pw)
        while (True):
            delete()

    except Exception as e:
        print(str(e))

    finally:
        os.system("Pause")
        # driver.quit()


def _login(driver, id, pw):
    script = "                                      \
        (function execute(){                            \
            document.querySelector('#id').value = '" + id + "'; \
            document.querySelector('#pw').value = '" + pw + "'; \
        })();"
    driver.execute_script(script)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#log\.login"))
    )
    element.click()


def delete():
    driver.get("https://n.news.naver.com/article/comment/346/0000050936#user_comment")
    option = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[5]/div[4]/ul/li[1]/div[1]/div/div[1]/span/span/a'))
    )

    print(option)
    option.click()

    delBtn = driver.find_element(By.CLASS_NAME, 'u_cbox_in_delete')
    delBtn.click()

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    except Exception as e:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        delete()
        print(e)

if __name__ == '__main__':
    main()
