import time
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

IS_DEBUG = True
USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]


def init_driver():
    # 不显示图形化界面
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')

    # local desktop
    # driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()

    # server
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=option)

    return driver


def process(driver, username, password):
    try:
        driver.get("http://stuinfo.neu.edu.cn/#/")

        # 输入用户名和密码，点击登录
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[2]/div[1]/input').send_keys(username)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/button').click()

        if IS_DEBUG:
            print("Login " + str(username) + " successful")

        # 定位
        ActionChains(driver).move_by_offset(100, 230).click().perform()
        ActionChains(driver).move_by_offset(0, 0).click().perform()
        ActionChains(driver).move_by_offset(0, 0).click().perform()

        time.sleep(1)

        ActionChains(driver).move_by_offset(300, 0).click().perform()

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        if IS_DEBUG:
            print("Switch to form")

        driver.find_element_by_css_selector("#sfgcyiqz").send_keys("否")
        driver.find_element_by_name("hjnznl").clear()
        driver.find_element_by_name("hjnznl").send_keys("家里")
        driver.find_element_by_name("qgnl").clear()
        driver.find_element_by_name("qgnl").send_keys("无")
        driver.find_element_by_css_selector("#sfqtdqlxs").send_keys("否")
        driver.find_element_by_css_selector("#sfjcgbr").send_keys("否")
        driver.find_element_by_css_selector("#sfjcglxsry").send_keys("否")
        driver.find_element_by_css_selector("#sfjcgysqzbr").send_keys("否")
        driver.find_element_by_css_selector("#sfjtcyjjfbqk").send_keys("否")
        driver.find_element_by_css_selector("#sfqgfrmz").send_keys("否")
        driver.find_element_by_css_selector("#sfygfr").send_keys("无")
        driver.find_element_by_css_selector("#sfyghxdbsy").send_keys("无")
        driver.find_element_by_css_selector("#sfygxhdbsy").send_keys("无")

        driver.find_element_by_xpath('/html/body/div[1]/div/div/button').click()

        time.sleep(2)
    except Exception as e:
        if IS_DEBUG:
            print(e)

        with open("log.txt", "a") as f:
            f.write("Error Occurred: line" + str(e.__traceback__.tb_lineno) + " - " + str(e))


def stop_driver(driver):
    driver.quit()

    if IS_DEBUG:
        print("Finished!")

    with open("log.txt", "a") as f:
        f.write("Complete the form: " + str(sys.argv[1]) + "\n")


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    driver = init_driver()
    process(driver, username, password)
    stop_driver(driver)
