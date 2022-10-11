import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'


def make_url(phone_number, text):
    return f"https://web.whatsapp.com/send?phone={phone_number}&text={text}&app_absent=1"


def automatic_send_message(phone_number, text):
    driver = webdriver.Chrome(ChromeDriverManager(version="105.0.5195.52").install(), chrome_options=chrome_options)
    url = make_url(phone_number, text)
    driver.get(url)

    send_button_present = EC.presence_of_element_located((By.XPATH, send_button_xpath))
    WebDriverWait(driver, timeout=30).until(send_button_present)

    send_button = driver.find_element(by=By.XPATH, value=send_button_xpath)
    send_button.click()
    time.sleep(1)

    driver.close()
    return f"Message was successfully sent to the phone number: {phone_number}"
