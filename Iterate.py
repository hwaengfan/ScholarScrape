from selenium import webdriver
from prettytable import PrettyTable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Iterate:
    def __init__(self, driver, directories, keywords):
        self.driver = driver
        self.directories = directories
        self.keywords = keywords

    # Wait for a xpath to appear

    def wait(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Go back to the previous section
    def goBack(self, sectionXpath):
        self.wait(sectionXpath)
        self.driver.find_element_by_xpath(sectionXpath).click()

    # Loop through each matched items in list
    def loopThrough(self, matchItems):
        listXpath = '/html/body/div[1]/div[5]/ul'
        self.wait(listXpath)
        listItems = self.driver.find_element_by_xpath(
            listXpath).find_elements_by_tag_name('li')
        for listItem in listItems:
            if listItem.text in matchItems:
                matchItems.remove(listItem.text)
                listItem.click()
                return True
            else:
                continue
        # When everything is looped through
        return False

    # Loop through each directories
    def iterateDirectories(self):
        directoriesCount = len(self.directories)
        for _ in range(directoriesCount):
            # Loop through keywords and return to previous section
            if(self.loopThrough(self.directories)):
                if(self.iterateKeywords()):
                    continue
                else:
                    self.goBack('/html/body/div[1]/div[4]/div/a[4]')
            else:
                return

    # Loop through each keywords
    def iterateKeywords(self):
        keywordsCount = len(self.keywords)
        for _ in range(keywordsCount):
            # Loop through scholarships and return to previous section
            if(self.loopThrough(self.keywords)):
                self.extractScholarships()
                self.goBack('/html/body/div[1]/div[4]/div/a[5]')
                continue
            else:
                self.goBack('/html/body/div[1]/div[4]/div/a[4]')
                return True

    # Write on output.txt
    def extractScholarships(self):
        table = PrettyTable(['Name', 'Amount', 'Due Day', 'Link'])
        tableXpath = '/html/body/div[1]/div[5]/table/tbody/tr'
        items = self.driver.find_elements_by_xpath(tableXpath)
        for item in items:
            titleElement = item.find_element_by_tag_name('a')
            amountElement = item.find_element_by_class_name('scholamt')
            dueDateElement = item.find_element_by_class_name('scholdd')
            table.add_row([titleElement.text, amountElement.text,
                          dueDateElement.text, titleElement.get_attribute('href')])

        f = open('output.txt', 'a')
        f.write(str(table))
        f.close()
