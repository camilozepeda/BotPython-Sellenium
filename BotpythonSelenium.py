import json
import re
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from   selenium.common.exceptions import NoSuchElementException
from   selenium.webdriver.common.by import By



def Get_Items(url_search):

    browser     = webdriver.Chrome()
    browser.get(url_search)

    while(True):
        current_page = browser.find_element_by_class_name('pagination').find_element_by_class_name('active')
        num_page     = int(current_page.text)+1
        #print("current page is %s" %(current_page.text))
        
        try:
            items =  browser.find_elements_by_css_selector("div[class*=info-box]")
            for values in items:
                out = [item for item in filter(None, values.text.split('\n'))]
                print(json.dumps(out))
            try: 
                button_modal = browser.find_element_by_class_name('acsCloseButton')
                #print("Encontre el modal")
                button_modal.click()
            except:
                print("No encontre el modal")
            try:
                next_page    = browser.find_element_by_class_name("pagination").find_element_by_link_text(str(num_page))
                next_page.click()
                
                try:
                    browser.get(browser.current_url)
                    #browser.implicitly_wait(10) # seconds
                except:
                   #print("No pude obtener url")
                    browser.close()
                    break
        
            except:
                #print("No existe pagina")
                #AQUi TERMINA EL BOT, UNA VEZ ENCUENTRA TODA LA DATA
                browser.close()
                break
        except:
                #print("No Encontre Items")
                browser.close()
                break





