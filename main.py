import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from time import sleep
import chromedriver_autoinstaller
from random import randint

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists

def launchBrowser():
    driver = webdriver.Chrome()
    driver.get("https://tinder.com")
    return driver

driver = launchBrowser()
sleep(10)

#click login
try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
except Exception as e:
    print(f"Something went wrong when click on Login: {e}")
    sys.exit()

sleep(15)

fb_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
if fb_button.get_attribute("aria-label") != "Login with Facebook" and fb_button.get_attribute("aria-label") != "Zaloguj się przez Facebooka":
    print(f'Wrong login form selected: {fb_button.get_attribute("aria-label")}')
else:
    fb_button.click()

sleep(15)

base_window = None
fb_login_window = None

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "Tinder" in driver.title:
        base_window = handle
    elif "Facebook" in driver.title:
        fb_login_window = handle

driver.switch_to.window(fb_login_window)

#FB Login section
sleep(10)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()
sleep(5)
driver.find_element(By.ID, 'email').send_keys("mihaiu.mihaukov@gmail.com")
driver.find_element(By.ID, 'pass').send_keys("#XbWerq-_66ZCF8")
driver.find_element(By.ID, 'loginbutton').click()
sleep(10)

#Back to Tinder
driver.switch_to.window(base_window)
sleep(5)
#Enable localization
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
sleep(10)
# Disable notifications
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()
sleep(10)
# Reject cookies
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button').click()
sleep(15)

#Liking
for _ in range(100):
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button').click()
    except exceptions.NoSuchElementException:
        print("Trying once more...")
        try:
            driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
        except exceptions.NoSuchElementException:
            print("Last chance...")
            try:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button').click()
            except Exception as e:
                print(f"I am giving up...: {e}")
                driver.refresh()
                sleep(randint(5, 10))
                continue
        except exceptions.ElementClickInterceptedException as e:
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[3]/button[2]').click()
            except exceptions.NoSuchElementException:
                try:
                    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]').click()
                except exceptions.NoSuchElementException:
                    print(f"Unrecognized pop up")
                    driver.refresh()
                else:
                    print(f"But Tinder plus pop up was shown. Probably no more likes, finishing...")
                    break
            else:
                print("First like pop up was shown")
                sleep(randint(5, 10))
    except Exception as e:
        print(f"Unrecognized exception: {e}")
        driver.refresh()
        sleep(randint(5, 10))
        continue

    sleep(randint(10, 12))
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button').click()
    except exceptions.NoSuchElementException:
        print(f"No like")
    except Exception as e:
        print(f"Unrecognized exception: {e}")
        driver.refresh()
        sleep(randint(5, 10))
    else:
        print("You have a like You handsome boi")
        sleep(randint(5, 10))

