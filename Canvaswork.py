# make sure to have chrome web driver installed in the same folder for ease of access
import pandas as pd
from selenium import webdriver
import numpy as py
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.action_chains import ActionChains

#stuff needed to make this work


# videohandle = pd.read_csv(r'C:\Users\garam masala 3.0\Desktop\canvas test grab\video list.csv')
# fhand for video list, not needed in this instance
print("----------------")
service = Service('/Users/rahil007/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
#driver_location = webdriver.Chrome(executable_path='C:/Users/rahil007/Downloads')# location of the webdriver, make sure that the version your current chrome is the same version of the webdriver
#driver = webdriver.Chrome(driver_location)


# url = "https://berkeley.idp.cirrusidentity.com/module.php/core/loginuserpass.php?AuthState=_888b30d1ae71d3872ce808e2e8a32b38dd95bd4528%3Ahttps%3A%2F%2Fberkeley.idp.cirrusidentity.com%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fberkeley.proxy.cirrusidentity.com%252Fsp%26cookieTime%3D1593726949"
url = "https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%26rlz%3D1C5CHFA_enUS790US790%26oq%3Dgoogle%2B%2B%26aqs%3Dchrome..69i57j69i59j69i60l3.2140j0j9%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)
# course url
actions = ActionChains(driver)
sleep(3)
actions.send_keys('rahilkapadia007@gmail.com').send_keys(Keys.ENTER)
actions.perform()
sleep(20)
print("Click the number")


url = "https://bcourses.berkeley.edu/courses/1487777/modules"
driver.get(url)

#opens up question bank
sleep(10)
url = "https://bcourses.berkeley.edu/courses/1487777/question_banks/2405409"
driver.get(url)
sleep(5)
#clicks the top to start the copy paste 
driver.find_element_by_id('questions').click()
#click and holds
Actions clkAndHld = new Actions(driver);
clkAndHld.clickAndHold(WebElement).build().perform();
#This will go through the questions move down and click on the more questions link and copy paste
while driver.find_elements_by_css_selector('.more_questions_link3'):
   
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    action.send_keys(Keys.COMMAND)
    action.send_keys(Keys.'c')
    driver.find_elements_by_css_selector('.more_questions_link').click
    #!!!!! STILL NEED TO FIGURE OUT HOW TO RELEASE THE CLICK HOLD AND THEN PLACE AGAIN AFTER CLICKING ON MORE_QUESTIONS LINK.
    sleep(3)






#if driver.find_element_by_id ("quiz_title") = True:
    



# driver.find_element_by_id('password').click()
# enter password in send keys string, region below is collapsed for passcode privacy
# region
# driver.find_element_by_id('password').send_keys("Metadata11")
# # endregion
# driver.find_element_by_css_selector('.btn').click()


#sleep(90)
#driver.quit()
# navigate to modules, use if statement in real thing
#USE XPATH FINDER EXTENSION




# driver.find_element_by_css_selector('.modules').click()
# driver.find_element_by_xpath('#context_module_item_15872925 > .ig-row > .ig-info > .module-item-title > .item_name > .ig-title').click()

#sleep(5)
