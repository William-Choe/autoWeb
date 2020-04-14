import time
import sys
from selenium import webdriver

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
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()

    # server
    # driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=option)

    return driver


def process(driver, username, password):
    try:
        driver.get("https://ehall.neu.edu.cn/db_portal/guide?id=D06BDA87-2E6E-4324-A14D-3BFAD839F2B9")

        # 点击我要办理
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/input[2]').click()

        # 转换到登录页面
        driver.switch_to.window(driver.window_handles[1])

        # 输入学号和密码
        driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[1]/input[1]').send_keys(username)
        driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[1]/input[2]').send_keys(password)

        # 登录
        driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div[1]/span/input').click()

        if IS_DEBUG:
            print("Login " + str(username) + " successful")

        # 填报信息
        driver.find_element_by_xpath('/html/body/div[1]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()

        # 上报
        driver.find_element_by_xpath('/html/body/div[1]/main/div/form/div[6]/button').click()

        time.sleep(2)
    except Exception as e:
        if IS_DEBUG:
            print(e)

        with open("log.txt", "a") as f:
            f.write("Error Occurred: line" + str(e.__traceback__.tb_lineno) + " - " + str(e))


def stop_driver(driver):
    # 获取上报完成标签
    label = driver.find_elements_by_xpath('/html/body/div[1]/main/div/div/div/div/div[1]')

    if IS_DEBUG:
        print(label[0].text)

    with open("log.txt", "a") as f:
        if label[0].text == "上报成功":
            f.write("Complete the form: " + str(sys.argv[1]) + "\n")
        else:
            f.write("Fail to complete\n")

    driver.quit()


if __name__ == '__main__':
    driver = init_driver()
    process(driver, USERNAME, PASSWORD)
    stop_driver(driver)
