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
url = "" #Place best buy item url here

email = "" #Plcae email address here
phoneNumber = "" #Place Phone Number here

FirstName = "" #Place first name here
LastName = "" #Place last name here


Address = "" # Place address here
Town = "" #Place town here
State = "" #Place state here
Zipcode = "" #Place local zipcode here


ccNum = "" #Place credit card number here (Dont type any - marks.)
ccExperationMonth = "" #Place credit card experation month here -- If it expires in Feburary, this field will be 02
ccExperationYear = "" #Place credit card experation year here -- If it expires in 2023, this field will be 23
cvv = "" #Place CVV here

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
    try:
        WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"go-to-cart-button")))
        browser.find_element(By.CLASS_NAME,"go-to-cart-button").click()
    except:
        WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"cart-icon")))
        browser.find_element(By.CLASS_NAME,"cart-icon").click()
    #browser.find_element_by_class_name("cart-icon").click();
    WebDriverWait(browser,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"checkout-buttons__checkout")))
    browser.find_element(By.CLASS_NAME,"checkout-buttons__checkout").click()
    
    
    #browser.find_element_by_class_name("checkout-buttons__checkout").click();
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"button-wrap")))
    browser.find_element(By.CLASS_NAME,"button-wrap").click()
    #browser.find_element_by_class_name("button-wrap").click();

    #browser.find_element(By.)

    #---- Fills in email address and phone number
    print("Filling in email address and phone number")
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"tb-input")))

    #browser.find_element(By.XPATH,"/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[2]/div[1]/fieldset/span/span/button").click()

    time.sleep(3)
    Elements = browser.find_elements(By.CLASS_NAME,"tb-input")



    firstNameElement = Elements[0]
    for c in FirstName:
        time.sleep(random.randint(1, 10)/100)
        firstNameElement.send_keys(c)

    WebDriverWait(browser,random.randint(1,10)/100)
    lastNameElement = Elements[1]
    for c in LastName:
        time.sleep(random.randint(1,10)/100)
        lastNameElement.send_keys(c)

    AddressElement = Elements[2]
    for c in Address:
        time.sleep(random.randint(1,10)/100)
        AddressElement.send_keys(c)

    cityElement = Elements[3]
    for c in Town:
        time.sleep(random.randint(1,10)/100)
        cityElement.send_keys(c)

    stateElement = Elements[4]
    for c in Zipcode:
        time.sleep(random.randint(1,10)/100)
        stateElement.send_keys(c)

    emailElement = Elements[5]
    for c in email:
        time.sleep(random.randint(1,10)/100)
        emailElement.send_keys(c)

    phoneElement = Elements[6]
    for c in phoneNumber:
        time.sleep(random.randint(1,10)/100)
        phoneElement.send_keys(c)


    select = Select(browser.find_element(By.CLASS_NAME,"tb-select"))
    select.select_by_visible_text('DE')

    browser.find_element(By.CLASS_NAME,"button--continue").click()

    #---- Payment Screen
    WebDriverWait(browser,10).until(expected_conditions.presence_of_element_located((By.ID,"optimized-cc-card-number")))
    ccElement = browser.find_element(By.ID,"optimized-cc-card-number")
    
    
    
    time.sleep(5)

    for c in ccNum:
        time.sleep(random.randint(10,100)/100)
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
    
    browser.find_element(By.CLASS_NAME,"payment__order-summary")
    print("Bought Item")


    print("Done")




bought = 0
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(url)
while(bought == 0):
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    if(len(soup(text="Add to Cart")) > 0):
        try:
            buyCode()
            bought = 1
        except:
            print("Buycode failed, trying again in one minute")
    else:
        print("Itme not in stock at: " + str(datetime.now()) + ", retrying in 1 minute")
    time.sleep(60)
    browser.refresh()
print("Program Stopped")
