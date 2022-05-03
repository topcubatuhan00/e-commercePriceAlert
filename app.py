import os
from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import smtplib

username = '' # mail adresi
password = '' # mail şifresi

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(username, password)

productLink = input("Link : ")
productPrice = input("Price You Expected : ")
mailAdress = input("The e-mail address to which the notification message will be sent : ")

if 'trendyol' in productLink or 'gittigidiyor' in productLink:
    condition = True

    browserOptions = webdriver.ChromeOptions()
    browserOptions.add_argument("--incognito")
    browserOptions.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=browserOptions,
                            executable_path='C:/webdriver/chromedriver.exe')
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.delete_all_cookies()

    action = ActionChains(driver)
else:
    print('Sadece Trendyol veya Gittigidiyor Linki Giriniz')
    condition = False

def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


while condition:
    try:
        driver.get(productLink)
    except selenium.common.exceptions.WebDriverException as e:
        print("Error")
        continue

    time.sleep(2)
    scroll()
    time.sleep(2)

    if 'trendyol' in productLink:
        productNewName = driver.find_element(
            by=By.CLASS_NAME, value='pr-new-br').text
        productNewPrice = driver.find_element(
            by=By.CLASS_NAME, value='prc-dsc').text
        productNewPrice = productNewPrice.replace(",", ".").split(" ")[0]
        os.system("cls")
    elif 'gittigidiyor' in productLink:
        productNewName = driver.find_element(by=By.ID, value='sp-title').text
        productNewPrice = driver.find_element(
            by=By.ID, value='sp-price-lowPrice').text
        productNewPrice = productNewPrice.split(",")[0].replace(",", ".")
        os.system("cls")
    else:
        print('hatalı link')

    if float(productNewPrice) <= float(productPrice):
        mail.sendmail(username, mailAdress, f"The price of {productNewName} has been reduced. New price {productNewPrice}".encode('utf-8'))
        break
    else:
        pass
    
    time.sleep(10)
    
