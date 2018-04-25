
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from   selenium.common.exceptions import NoSuchElementException
from   selenium.webdriver.common.by import By
import BotpythonSelenium as bot 




browser  =  webdriver.Chrome()
url      =  "http://www.sodimac.cl/sodimac-cl/search/?Ntt=tuercas"  

browser.get(url)

#EJEMEPLO DE BUSQUEDA CON DOS ITEMS EN LISTA
items=['Tuercas','Martillos']

for item in items:
    try:
        search_button = browser.find_element_by_class_name('iconSearch-Responsive')  
        search_button.click()
        try:  
            search_input = browser.find_element_by_name('Ntt')
            search_input.clear()
            search_input.send_keys(item)
            search_input.submit()
            try: 
                button_modal = browser.find_element_by_class_name('acsCloseButton')
                #print("Encontre el modal")
                button_modal.click()
            except:
                print("No encontre el modal")
            try:
                url = browser.current_url
                bot.Get_Items(url)
            except:
                #print("no puedo traer la url del momento")
                browser.close()
        
        except:
            #print("no encontre el input")
            browser.close()
        
    except:
        #print("No encontre buscador ")
        browser.close()
browser.close()