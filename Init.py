from selenium import webdriver


class Init:
    def __init__(self, driver, userName, passWord):
        self.driver = driver
        self.userName = userName
        self.passWord = passWord

    # Open Google Chrome through chromedriver and go to the website
    def openBrowser(self, url):

        self.driver.maximize_window()
        self.driver.get(url)

    # Logging into account
    def logIn(self):
        userNameXpath = '/html/body/div/div[3]/div/div/form/div/div/div[1]/input'
        passWordXpath = '/html/body/div/div[3]/div/div/form/div/div/div[4]/input'
        self.driver.find_element_by_xpath(
            userNameXpath).send_keys(self.userName)
        self.driver.find_element_by_xpath(
            passWordXpath).send_keys(self.passWord)
        # Go to the directory section
        self.driver.get('https://www.scholarships.com/scholarship-directory')
