import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main(id, pw):
    # Chrome Driver 설정 (ChromeDriverManager를 통해 자동으로 다운로드 후 설정)
    def set_chrome_driver1():
        try:
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            return driver
        except:
            return set_chrome_driver()

    # WebDriver의 크롬드라이버 최신 155.x 버전 미호환 이슈로인해 다운로드가 안 될경우
    # 로컬에서 Chrome Driver 설정 (직접 경로를 통해 설정)
    def set_chrome_driver():
        driver = webdriver.Chrome(r'./chromedriver.exe')
        return driver

    driver = set_chrome_driver1()

    # 댓글 삭제를 위한 URL 설정
    URL = "https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fn.news.naver.com%2Farticle%2Fcomment%2F346%2F0000050936" \
          "&svctype=0"

    # 네이버 로그인 함수
    def _login(driver, _id, _pw):
        # JavaScript를 이용하여 ID, PW 입력
        script = "                                      \
            (function execute(){                            \
                document.querySelector('#id').value = '" + _id + "'; \
                document.querySelector('#pw').value = '" + _pw + "'; \
            })();"
        driver.execute_script(script)

        # 로그인 버튼 클릭
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#log\.login"))
        )
        element.click()

    # 댓글 삭제 함수
    def delete():
        driver.get("https://n.news.naver.com/article/comment/346/0000050936#user_comment")

        # 팝업 제거
        try:
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="_MODAL_COMMENT_FOLLOW_TUTORIAL"]/div/div/div[2]/div/div/button'))
            )
            element.click()
        except Exception:
            pass

        # 옵션 버튼 클릭
        option = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div/div[2]/div/div[2]/div[5]/div[4]/ul/li[1]/div[1]/div/div[1]/span/span/a'))
        )
        option.click()

        # 삭제 버튼 클릭
        delBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'u_cbox_in_delete'))
        )
        delBtn.click()

        # 알림 팝업에서 확인 버튼 클릭
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        except Exception as e:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            delete()
            print(e)
            driver.quit()

    # 프로그램 실행 부분
    try:
        driver.get(URL)
        _login(driver, id, pw)
        while True:
            delete()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
