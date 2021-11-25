from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from bs4 import BeautifulSoup
import random
import time








print("Initializing Settings")


#----------  settings ------------
FirstName = "Type First Name Here" #Place first name here
LastName = "Type Last Name Here" #Place last name here
email = "Type Email Here" #Place full email address here
phoneNumber = "Type Phone Number Here" #Place phone number here. This will work with and without the - marks
Address = "Type Address Here" #Place address here
Town = "Type Town Here" #Place town here
State = "Type State Code Here" #Place two digit state code here. As an example, Delaware is DE
Zipcode = "Type Zipcode Here" #Place zip code here
url = 'Type URL Here' #Place Best Buy item url here
ccNum = "Type CC Number Here" #Place credit card number here 
ccExperationMonth = "Type month here" #Place credit card experation month here. If the month is September, type 09. 
ccExperationYear = "Type year Here" #Place credit card experation year here. 
cvv = "Type cvv Here" #Place credit card cvv number here. This should be a 3 digit number. 

refreshTime = 60 #This is how often (in seconds) the bot will refresh the page. This should be set to 60 seconds by default

# ----------- End of settings ---------


print("Done initializing settings")

def buyCode():
    
    # ----------- Adding item to cart -------
    print("adding item to cart")
    WebDriverWait(browser,3)
    WebDriverWait(browser,20).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"add-to-cart-button")))
    time.sleep(2)
    browser.find_element(By.CLASS_NAME,"add-to-cart-button").click()
    #This sleep gives the webpage time to process the add to cart request
    time.sleep(2)

    

    #browser.find_element_by_class_name("add-to-cart-button").click();

    #---------- Navigating to purchase screen -----
    print("Going to checkout screen")
    
    #Best Buy's website can do two different things at this point. It can either do nothing, or it can create a pop up window. This try catch statement handles both possibilities
    try:
        WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"go-to-cart-button")))
        browser.find_element(By.CLASS_NAME,"go-to-cart-button").click()
    except:
        WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"cart-icon")))
        browser.find_element(By.CLASS_NAME,"cart-icon").click()
    
    #This sleep gives the webpage some time to process the go to cart reqest. 
    time.sleep(2)
    
    #This wait will wait 10 seconds, or wait until the checkout button is clickable. 
    WebDriverWait(browser,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"checkout-buttons__checkout")))
    
    #This will click the checkout button
    browser.find_element(By.CLASS_NAME,"checkout-buttons__checkout").click()
    
    
    
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"button-wrap")))
    browser.find_element(By.CLASS_NAME,"button-wrap").click()


    #---- Fills in personal infno
    print("Filling in personal information")
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"tb-input")))


    #Time to allow page to process request. 
    time.sleep(8)

    #Finds elements that need to be filled in.
    Elements = browser.find_elements(By.CLASS_NAME,"tb-input")


    #Filles in first name
    firstNameElement = Elements[0]
    for c in FirstName:
        time.sleep(random.randint(1, 10)/100)
        firstNameElement.send_keys(c)

    #Fills in last name
    WebDriverWait(browser,random.randint(1,10)/100)
    lastNameElement = Elements[1]
    for c in LastName:
        time.sleep(random.randint(1,10)/100)
        lastNameElement.send_keys(c)

    #Fills in address
    AddressElement = Elements[2]
    for c in Address:
        time.sleep(random.randint(1,10)/100)
        AddressElement.send_keys(c)

    #Fills in city
    cityElement = Elements[3]
    for c in Town:
        time.sleep(random.randint(1,10)/100)
        cityElement.send_keys(c)

    #Fills in zipcode
    stateElement = Elements[4]
    for c in Zipcode:
        time.sleep(random.randint(1,10)/100)
        stateElement.send_keys(c)

    #Fills in email
    emailElement = Elements[5]
    for c in email:
        time.sleep(random.randint(1,10)/100)
        emailElement.send_keys(c)

    #Fills in phone number
    phoneElement = Elements[6]
    for c in phoneNumber:
        time.sleep(random.randint(1,10)/100)
        phoneElement.send_keys(c)


    select = Select(browser.find_element(By.CLASS_NAME,"tb-select"))
    select.select_by_visible_text(State)

    browser.find_element(By.CLASS_NAME,"button--continue").click()

    #Try except block used as an attempt to bypass changing shipping time
    time.sleep(3)
    WebDriverWait(browser,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"button--continue")))
    try:
        browser.find_element(By.CLASS_NAME,"button--continue").click()
    except:
        print("Already on payment screen")




    #---- Payment Screen
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.ID,"optimized-cc-card-number")))
    ccElement = browser.find_element(By.ID,"optimized-cc-card-number")
    
    
    
    time.sleep(5)

    for c in ccNum:
        time.sleep(random.randint(1,100)/100)
        ccElement.send_keys(c)
    
    #CVV boxes only appear after typing in cc number
    cvvElements = browser.find_elements(By.CLASS_NAME,"tb-select")
    cvvMonthElement = Select(cvvElements[0])
    cvvYearElement = Select(cvvElements[1])

    cvvMonthElement.select_by_visible_text(ccExperationMonth)
    cvvYearElement.select_by_visible_text(ccExperationYear) #credit-card-cvv
    
    cvvNumElement = browser.find_element(By.ID,"credit-card-cvv")
    
    for c in cvv:
        time.sleep(random.randint(10,100)/100)
        cvvNumElement.send_keys(c)
    
    browser.find_element(By.CLASS_NAME,"payment__order-summary").click()
    print("Bought Item")


    print("Done")





#Value used to stop the bot after one purchase
bought = 0

#Used to install and open the webdriver
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#Opens the provided url in the webdriver
browser.get(url)

#Cheks webpage once per provided refreshTime period for in stock items. Loop will stop if item is sucesfully purchased. 
while(bought == 0):
    
    #Gets the page html and look for Add to cart button
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Checks cart to see if item is in stock
    if(len(soup(text="Add to Cart")) > 0):
        #If the item is in stock, try to run the buyCode function
        try:
            buyCode()
            bought = 1
        except:
            print("Buycode failed, trying again in one minute")
    else:
        print("Itme not in stock at: " + str(datetime.now()) + ", retrying in 1 minute")
    
    #Sleeps for the provided refresh time, and refreshes the page
    time.sleep(refreshTime)
    browser.refresh()


#Program should end when one item is purchased
print("Program Stopped")



