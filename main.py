# python = 3.6
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


# TODO: EDIT ID PASSWD
SCHOOLID = '202222222222'
PASSWD = 'qwerty123'

# DO NOT EDIT
EDGE = 0
CHROME = 1
FIREFOX = 2
# DO NOT EDIT

# TODO: EDIT DRIVER PATH

DRIVER = CHROME  # 代表着你选用了Chrome
DRIVER_PATH = "C:\\Data\\chromedriver.exe"


def isConnectedNet():
    # if os.name == 'nt':
    #     return os.system("ping baidu.com -n 1 -w 1")
    # else:
    #     return os.system("ping baidu.com -w 1")

    # TUN MOD会劫持ping命令，现在使用curl命令代替ping判断是否连接
    # 不用TUN MOD的话，用上面的命令更节约资源
    myre = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    try:
        _ip = os.popen("curl 4.ipw.cn").readline().strip()
        print(_ip)
        # print(myre.match(_ip).group())
        # print(myre.match(_ip).group() == _ip)
        return myre.match(_ip).group() == _ip
    except Exception:
        return False


def main():
    if isConnectedNet():
        return 1
    cnt = 0
    if DRIVER == 0:
        print("Using Edge")
        from selenium.webdriver.edge.service import Service as Se
        service = Se(DRIVER_PATH)
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Edge(service=service, options=options)
    if DRIVER == 1:
        print("Using Chrome")
        from selenium.webdriver.chrome.service import Service as Se
        service = Se(DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=service, options=options)
    elif DRIVER == 2:
        print("Using Firefox")
        from selenium.webdriver.firefox.service import Service as Se
        service = Se(DRIVER_PATH)
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Firefox(service=service, options=options)
    while (not isConnectedNet()):
        print("Un connect")
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
            return -1
    return 1


if __name__ == "__main__":
    main()


# pyinstaller -Fw main.py
