from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

def openPage(url):
      opt = Options()
      opt.add_argument('--headless')
      opt.add_argument('--disable-gpu')
      
      browser = webdriver.Chrome(chrome_options = opt)
      browser.get(url)
      return browser

def login(browser,username, password):
      usr = browser.find_element_by_id("username")
      usr.send_keys(username)

      psw = browser.find_element_by_id("password")
      psw.send_keys(password)

      loginbtn = browser.find_element_by_id("dl")
      loginbtn.click()

def hitCard(browser):
      radio1 = browser.find_element_by_xpath("//div[@name='sfzx']/div/div[2]")
      radio1.click()

      sleep(2)

      addrs = browser.find_element_by_xpath("//div[@name='area']/input")
      addrs.click()

      sleep(7)

      radio2 = browser.find_element_by_xpath("//div[@name='sfymqjczrj']/div/div[2]")
      radio2.click()

      sleep(2)

      radio3 = browser.find_element_by_xpath("//div[@name='sfqrxxss']/div/div/span")
      radio3.click()

      sleep(1)
      
      btn = browser.find_element_by_xpath("//div[@class='footers']/a")
      btn.click()

      sleep(2)

      btn2 = browser.find_element_by_xpath("//div[@class='wapcf-btn-box']/div[2]")
      btn2.click()

if __name__ == "__main__":
      bs=openPage("https://healthreport.zju.edu.cn/ncov/wap/default/index")
      sleep(2)
      login(bs, "Sno", "Psw")
      sleep(7)
      hitCard(bs)
      sleep(2)
      bs.close()
