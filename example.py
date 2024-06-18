import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from time import sleep
import requests
from PIL import Image
from io import BytesIO
import easyocr
from selenium.webdriver.common.by import By

def initDriver():
    options = uc.ChromeOptions()
    options.headless = False # Set to 'True' to disable GUI
    
    driver = uc.Chrome(options=options)

    return driver


def getPage(driver, url):
    with driver:
        driver.get(url.strip())


def extractText(image_link):
    print(f"Image link : {image_link}") # Image dimensions are 200 x 70
    response = requests.get(image_link)
    img = Image.open(BytesIO(response.content))

    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)

    extracted_text = '\n'.join([text[1] for text in result])
    print("Extracted Text:")
    print(extracted_text)

    return extracted_text


def solveCaptcha(driver):
        print("Captcha triggered!")
        image_link = captcha_image.img["src"].strip()

        extracted_text = extractText(image_link)
        """if len(extracted_text)!=6:
             solveCaptcha(driver)"""
        
        # Fill the input field
        text_field = driver.find_element(By.CLASS_NAME, 'a-span12')
        for letter in extracted_text:
            text_field.send_keys(letter)
            sleep(0.37)
        submit_button = driver.find_element(By.CLASS_NAME, 'a-button-text')
        sleep(0.66)
        submit_button.click()


driver = initDriver()
url = "https://www.amazon.com"

getPage(driver, url)
sleep(2)
    
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

captcha_image = soup.find('div', class_='a-row a-text-center')
if captcha_image:
     solveCaptcha(driver)