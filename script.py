# Procedures:
# go to scholarships.com
# log in and use filter provided there
# filter in scholarship.com:
# loop through each <li> (element list) in <ul> and go through <li> that has key words provided
# key words ex: computer engineering, computer science, asian, senior, etc.
# output the whole table
# go through each link in the table to get description
# output a file that contains all the info: name, amount, due day, and link

# Import modules
import linecache
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open file to get info to log in


def input_info(line1, line2):
    # C:\Users\Hoang\Desktop\Projects\Python\WebScraping\Scholarships
    file = open(
        r'C:\Users\Hoang\Desktop\Projects\Python\WebScraping\Scholarships\Info.txt', 'r')
    user = linecache.getline('Info', line1)
    key = linecache.getline('Info', line2)
    file.close()
    return user, key

# Wait for an element to load up


def wait(xpath):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

# Scholarships.com:
# Count how many times need to go through the unordered list


def loop(keywords=[]):
    wait('/html/body/div[1]/div[6]/ul')
    requirements = driver.find_element_by_xpath('/html/body/div[1]/div[6]/ul')
    counts = 0
    for requirement in requirements.find_elements_by_tag_name('li'):
        if requirement.text in keywords:
            counts += 1
    return counts


def gothrough(keywords=[]):
    wait('/html/body/div[1]/div[6]/ul')
    requirements = driver.find_element_by_xpath('/html/body/div[1]/div[6]/ul')
    for requirement in requirements.find_elements_by_tag_name('li'):
        if requirement.text in keywords:
            keywords.remove(requirement.text)
            requirement.click()
            return keywords
        else:
            continue


def gothrough_filtertypes():
    keywords = ['Academic Major', 'Ethnicity', 'Financial Need', 'Grade Point Average', 'Race', 'Religion',
                'Residence State', 'School Year', 'Special Attributes', 'Student Organization'
                ]
    counts = loop(keywords)
    for _ in range(counts):
        gothrough(keywords)
        gothrough_filteroptions()
        wait('/html/body/div[1]/div[5]/div[1]/a[4]')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[5]/div[1]/a[4]').click()
        print(keywords)
    print('Done')


def gothrough_filteroptions():
    keywords = ['Computer Engineering', 'Computer Science', 'American', 'Vietnamese', 'Financial Need Required',
                'Minimum Grade Point Average From 3.6 to 4.0', 'Asian/Pacific Islander', 'Catholic', 'California',
                'High School Junior (H.S. Class of 2021)', 'Bilingual', 'First In Family College Student',
                'Left-Handed People', 'Tall People', 'American Red Cross'
                ]
    counts = loop(keywords)
    for _ in range(counts):
        gothrough(keywords)
        extract_data()
        wait('/html/body/div[1]/div[5]/div[1]/a[5]')
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[5]/div[1]/a[5]').click()
        print(keywords)


def extract_data():
    t = PrettyTable(['Name', 'Amount', 'Due Day', 'Link'])
    for a in driver.find_elements_by_xpath('/html/body/div[1]/div[6]/table/tbody/tr'):
        t.add_row([a.find_element_by_tag_name('a').text, a.find_element_by_class_name('scholamt').text,
                   a.find_element_by_class_name('scholdd').text, a.find_element_by_tag_name(
                       'a').get_attribute('href'),
                   ])

    f = open('Output.txt', 'a')
    f.write(str(t))
    f.close()
    print('extracted')

# Extract data from scholarships.com (whole procedure)


def scholarships(url):
    # open web
    driver.get(url)
    # get input info
    user, key = input_info(1, 2)
    # log in
    driver.find_element_by_xpath(
        '/html/body/div/div[3]/div/div/form/div/div/div[1]/input').send_keys(user)
    driver.find_element_by_xpath(
        '/html/body/div/div[3]/div/div/form/div/div/div[4]/input').send_keys(key)
    # go to scholarship directory
    driver.get('https://www.scholarships.com/scholarship-directory')
    # extract data
    gothrough_filtertypes()
    print('Done')
    return


# Run Google Chrome and call function
# Open Google Chrome
driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
driver.maximize_window()
# Go through scholarship.com
scholarships('https://www.scholarships.com/login')
driver.close()
