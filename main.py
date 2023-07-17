# python = 3.6
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


SCHOOLID = '2022222222222'
PASSWD = 'PASSWD'


def isConnectedNet():
    if os.name == 'nt':
        return os.system("ping baidu.com -n 1 -w 1")
    else:
        return os.system("ping baidu.com -w 1")


if __name__ == "__main__":
    cnt = 0
    while (isConnectedNet() != 0):
        if os.name == 'nt':
            from selenium.webdriver.edge.service import Service
            # from selenium.webdriver.chrome.service import Service as Se
            print("Using Edge")
            Se = Service("C:\\Data\\msedgedriver.exe")
            options = webdriver.EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Edge(service=Se, options=options)
        else:
            print("Using Firefox")
            # from selenium.webdriver.firefox.service import Service as Se
            options = webdriver.FirefoxOptions()
            # 设置火狐为headless无界面模式
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Firefox(options=options)

        driver.get('http://10.253.0.237/srun_portal_pc?ac_id=1&theme=dx')
        user_input = driver.find_element(
            by=By.XPATH, value='//input[@type="text"]')
        pw_input = driver.find_element(
            by=By.XPATH, value='//input[@type="password"]')
        login_btn = driver.find_element(
            by=By.ID, value='school-login')
        user_input.send_keys(SCHOOLID)
        pw_input.send_keys(PASSWD)
        time.sleep(0.5)
        login_btn.click()
        time.sleep(0.5)
        driver.quit()
        cnt += 1
        if cnt >= 3:
            break

# pyinstaller -Fw main.py
