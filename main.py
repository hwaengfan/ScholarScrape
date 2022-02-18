from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Init import Init
from Iterate import Iterate

# DELETE COMMENTS WHEN DONE (to prompt username and pass)
# Prompt username and pass
options = Options()
options.headless = True

# input('Enter username on Scholarship.com: ')
userName = '21hoangphan@gmail.com'
passWord = '04182003'  # input('Enter password on Scholarship.com: ')
driver = webdriver.Chrome(
    executable_path=r'C:\Chromedriver\chromedriver.exe', chrome_options=options)

# Initialize chrome and to go website
init = Init(driver, userName, passWord)
url = 'https://www.scholarships.com/login'
init.openBrowser(url)
init.logIn()

# Iterate through sections to find scholarships
directories = ['Academic Major', 'Ethnicity', 'Financial Need', 'Grade Point Average', 'Race',
               'Religion', 'Residence State', 'School Year', 'Special Attributes', 'Student Organization']  # add an option to choose later

keywords = ['Computer Engineering', 'Computer Science', 'American', 'Vietnamese', 'Financial Need Required',
            'Minimum Grade Point Average From 3.6 to 4.0', 'Asian/Pacific Islander', 'Catholic', 'California',
            'High School Junior (H.S. Class of 2021)', 'Bilingual', 'First In Family College Student',
            'Left-Handed People', 'Tall People', 'American Red Cross']  # add an option to choose later

iterate = Iterate(driver, directories, keywords)
iterate.iterateDirectories()

driver.close()
print('done')
