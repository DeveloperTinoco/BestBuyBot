import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
openBrowser = webdriver.Chrome(
    chrome_options=options, executable_path=r'E:\WebDriver\chromedriver.exe')


openBrowser.get(
    'INSERT URL LINK HERE FOR THE ITEM YOU WANT THE BOT TO PURCHASE')


def checkSuccess():
    buttonText = button.text
    success = True

    try:
        openBrowser.find_element_by_class_name('success')

    except:

        while success == True:

            if 'Add to Cart' in buttonText:
                success = False
            else:
                buttonText = button.text

        time.sleep(.5)
        addToCart()
    else:
        pass


def addToCart():
    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
    addCart = openBrowser.find_element_by_class_name('btn-primary')
    addCart.click()
    time.sleep(1.1)
    checkSuccess()
    print('In stock, added to cart!')


def goToCart():
    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'go-to-cart-button')))
    goCart = openBrowser.find_element_by_class_name(
        'go-to-cart-button')
    goCart.click()
    print('Going to cart.')


def goToCheckout():
    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'checkout-buttons')))
    checkout = openBrowser.find_element_by_class_name('btn-primary')
    checkout.click()
    print('Going to checkout.')


def signIn():
    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.ID, 'fld-e')))
    email = openBrowser.find_element_by_id(
        'fld-e').send_keys('INSERT EMAIL HERE THAT IS USED TO SIGN IN TO YOUR BEST BUY ACCOUNT')

    password = openBrowser.find_element_by_id(
        'fld-p1').send_keys('INSERT YOUR PASSWORD FOR BEST BUY HERE')

    signIn = openBrowser.find_element_by_class_name(
        'cia-form__controls__submit ')
    signIn.click()
    print('Signing back in.')


def placeOrder():
    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.ID, 'credit-card-cvv')))
    security_code = openBrowser.find_element_by_id(
        'credit-card-cvv').send_keys('INSERT YOUR CVV FROM YOUR CARD THAT IS ALREADY ON FILE HERE')

    orderButton = openBrowser.find_element_by_class_name('btn-primary')
    orderButton.click()
    print('Checkout Successful!')


while True:

    WebDriverWait(openBrowser, 3000).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'add-to-cart-button')))
    button = openBrowser.find_element_by_class_name('add-to-cart-button')
    isEnabled = button.is_enabled()

    if isEnabled == False:
        print('Not available yet.')
        time.sleep(.5)

    else:
        addToCart()
        goToCart()
        goToCheckout()
        signIn()
        placeOrder()
        time.sleep(600)
        openBrowser.quit()
