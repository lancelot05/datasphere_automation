# Importing packages
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def process(url,email,password,space,jsondir):
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver,30)

    path_of_the_csv_directory= os.getenv('CSV_DIR')
    path_of_the_json_directory= os.getenv('JSON_DIR')

    # Login process
    driver.find_element(By.ID,'j_username').send_keys(email)
    driver.find_element(By.ID,'j_password').send_keys(password)
    driver.find_element(By.ID,'logOnFormSubmit').click()

    # Navigating to data builder
    wait.until(EC.presence_of_element_located((By.ID,'__item5'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='{}']".format(space)))).click()

    # Importing JSON and loading data
    wait.until(EC.presence_of_element_located((By.ID,"shellMainContent---databuilderComponent---databuilderLandingPage--entitySelectionLandingPage--importEntity-internalBtn"))).click()
    wait.until(EC.presence_of_element_located((By.ID,"shellMainContent---databuilderComponent---databuilderLandingPage--entitySelectionLandingPage--importFileUploader-fu"))).send_keys(jsondir)
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='shellMainContent---databuilderComponent---databuilderLandingPage--addRepositoryObjectsDlg--tableSelectDialog-table-sa-CbBg']"))).click()
    wait.until(EC.presence_of_element_located((By.ID,"shellMainContent---databuilderComponent---databuilderLandingPage--addRepositoryObjectsDlg--tableSelectDialog-ok"))).click()   

    time.sleep(100)
    driver.back()


