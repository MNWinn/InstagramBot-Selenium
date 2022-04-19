import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv


class Bot:
    def __init__(self, email, password):
        s = Service('CHROMEDRIVERPATHr')
        self.driver = webdriver.Chrome(service=s)
        self.email = email
        self.password = password

    def signIn(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys(self.email)
        self.driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def getFollowers(self, username):
        try:
            self.driver.get('https://www.instagram.com/' + username + '/')
            self.driver.find_element(By.XPATH, "//*[text()='Follow']").click()
        except:
            print("Account has been added or needs to be followed back instead")



bot=Bot('USERNAME', 'PASSWORD')
bot.signIn()
time.sleep(5)

csv_file = 'NAMEOFCSV.csv'
with open(csv_file, 'r') as csv_file1:
    num_Reader = csv.reader(csv_file1)
    next(num_Reader)
    numbers = set(p[1] for p in num_Reader)

for i in numbers:
    bot.getFollowers(i)
    time.sleep(3)



time.sleep(20)