from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import ActionChains




def run():


    # url = r"https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python"
    # driver = webdriver.Safari()
    # driver.get(url)
    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # time.sleep(10)


    # driver = webdriver.Firefox()
    url = r"https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu"
    url2 = r"https://xmuxg.xmu.edu.cn/xmu/app/214"
    # driver = webdriver.Firefox(executable_path=r'D:\geckodriver-v0.28.0-win64\geckodriver.exe')
    driver = webdriver.Safari()

    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("23220191151287")
    time.sleep(0.5)
    driver.find_element_by_id("password").send_keys("300527")
    # driver.find_elements_by_xpath("//button[@class='auth_login_btn primary full_width']")[0].click()
    driver.find_elements_by_xpath("//button[@class='auth_login_btn primary full_width']")[0].send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键
    # time.sleep(10)
    # print("strat roll")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # print("stop roll")
    time.sleep(10)
    driver.get(url2)
    time.sleep(8)
    driver.find_elements_by_xpath("//div[@class='tab']")[0].click()
    time.sleep(5)

    ac = driver.find_element_by_id("pdfDom")
    ActionChains(driver).move_to_element(ac).click().perform()

    for i in range(14):
        print("send: ", i)
        ac.send_keys(Keys.DOWN)
        time.sleep(0.1)

    time.sleep(5)
    driver.find_element_by_xpath("//div[@date-name='select_1582538939790']")[0].click()
    driver.find_element_by_class_name("dropdown-items active").click()

if __name__ == '__main__':
    run()

