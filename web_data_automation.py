from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep
import logging as log

log.basicConfig(filename='./selenium.log', level=log.INFO, format  = '%(asctime)s %(name)s %(levelname)s %(message)s')

log.info("checking given chromedriver is working fine")
# Giving the path of chromedriver which downloaded from web
browser=webdriver.Chrome(executable_path="./chromedriver_linux64/chromedriver")
# setting of window size
browser.set_window_size(900,900)
# Setting of window position which is leftmost to 9 right
browser.set_window_position(0,9)

log.info("Passing url in browser")
# Passing the value of URL which needs to be open
browser.get("http://demo.guru99.com/test/web-table-element.php#")

# Get delayed for 5 second to open the browser
sleep(2)

try:
    log.info("Getting last updated value from browser")
    # Get the last updated value from browser
    lst_upd=browser.find_element_by_xpath("//*[@id='leftcontainer']/div[1]/div[2]/span")
    log.info(lst_upd.text)

    log.info("Getting variable company name")
    # Getting variable company name
    cmpny=browser.find_element_by_xpath("//*[@id='leftcontainer']/table/thead/tr/th[1]").text
    log.info(cmpny)

    log.info("Getting the list of company availabe in web page")
    # Getting the list of company availabe in web page
    table=browser.find_element_by_xpath("//*[@id='leftcontainer']/table").text
    log.info(table)

    log.info("Getting the SEO dropdown button")
    # Click the SEO dropdown button
    drop_down=browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul/li[11]/a").click()
    log.info(drop_down)

    log.info("Click the SEO dropdown button")
    # Click the SEO dropdown sub-menu button of Page-1
    sub_menu=browser.find_element_by_xpath("//*[@id='navbar-brand-centered']/ul/li[11]/ul/li[1]/a").click()
    log.info(sub_menu)

    log.info("Get the list of main navigation on Page-1 like [Home, Testing, SAP etc]")
    #Get the list of main navigation on Page-1 like [Home, Testing, SAP etc]
    main_nav=browser.find_element_by_xpath("//*[@id='menu-1072-particle']/nav").text
    log.info(main_nav)

    log.info("Click the Home menu-item from main_nav")
    # Click the Home menu-item from main_nav
    menu_title=browser.find_element_by_xpath("//*[@id='menu-1072-particle']/nav/ul/li[1]/a/span/span").click()

    log.info("Get the text of input box of email id")
    # Get the above text of input box of email id
    menu_title=browser.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td/h2").text

    title_text="""Enter your email address to get access details to demo site"""
    
    try:
        log.info("check assertion of len of title_text and menu_title")
        # check with assert if title_text is equal to menu_title
        assert(len(title_text) == len(menu_title))
    except Exception as e:
        log.info("Assertion Fail",e)
        print("Assertion Fail",e)

    log.info("Get the input box of email id")
    # Get the input box of email id
    email_id=browser.find_element_by_name("emailid")

    log.info("passing the value in input box")
    # passing the value in input box
    email_id.send_keys("test@gmail.com")

    log.info("Click the login button below input box")
    # Click the login button below input box
    email_id=browser.find_element_by_name("btnLogin").click()

    try:
        log.info("Get the message for user id and password on access details page")
        # Get the message for user id and password on access details page
        message=browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/h2").text

        log.info("check with assert if message is same as on access details page")
        # check with assert if message is same as on access details page
        assert("Access details to demo site." in message)

        log.info("get the uid")
        # get the uid and pwd
        usr_id=browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[2]").text
        log.info(usr_id)
        log.info("get the pwd")
        pwd=browser.find_element_by_xpath("/html/body/table/tbody/tr[5]/td[2]").text
        log.info(pwd)
        # print("user id : ",usr_id)
        # print("pwd : ",pwd)
    except Exception as e:
        log.info("Invalid email",e)
        print("invalied email",e)

    sleep(2)

    browser.close()
except Exception as e:
    log.info("Page not loaded",e)
    print("Page not loaded",e)