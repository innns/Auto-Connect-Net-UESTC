# Auto-Connect-Net-UESTC
电子科技大学自动连接校园网脚本，使用了Selenium 4，支持Ubuntu 和 Windows

# 使用方法

## 0x00 配置环境

按`requirements.txt`配置环境

```bash
# 如果你用 conda
conda create -n myenv
conda activate myenv

# 或者使用 venv
python3 -m venv myenv
## ubuntu
source ./test_env/bin/activate
## windows
.\test_env\Scripts\Activate.ps1

# 安装依赖
python -m pip install -r requirements.txt
```

配置 `WebDriver`

[Edge用户](https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium/?tabs=c-sharp)

[Firefox用户](https://github.com/mozilla/geckodriver)

[Chrome用户](https://chromedriver.chromium.org/)

**注意更改代码处的Driver路劲、所选的浏览器。建议使用 Edge**

## 0x01 设置学号、密码

更改`main.py`中的`SCHOOLID`，`PASSWD`为自己的学号密码

```python
SCHOOLID = '2022222222222'
PASSWD = 'PASSWD'
```

## 0x02 打包为可执行文件

```bash
conda activate myenv
pyinstaller -Fw main.py
```

生成的文件一般在`dist`文件夹下

## 0x03 设置自动执行

[windows 设置开机启动](https://support.microsoft.com/zh-cn/windows/%E5%9C%A8-windows-10-%E4%B8%AD%E6%B7%BB%E5%8A%A0%E5%9C%A8%E5%90%AF%E5%8A%A8%E6%97%B6%E8%87%AA%E5%8A%A8%E8%BF%90%E8%A1%8C%E7%9A%84%E5%BA%94%E7%94%A8-150da165-dcd9-7230-517b-cf3c295d89dd)

[windows 设置定时任务](https://zhuanlan.zhihu.com/p/430602325)

[Ubuntu 设置开机任务](https://zhuanlan.zhihu.com/p/496990810)

[Ubuntu 设置定时任务](https://zhuanlan.zhihu.com/p/350671948)

