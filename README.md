# python-sellenium-bot

pip install sellenium-webdriver   

pip install simplejson

instalar chromedriver https://chromedriver.storage.googleapis.com/index.html?path=2.38/
chromedriver debe estar en el mismo folder que el .py

#Dependencias del código
```python
import json
import re
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from   selenium.common.exceptions import NoSuchElementException
from   selenium.webdriver.common.by import By
```

#Conexiones a url ejemplo

Se hace uso de browser como variable contenedora del set webdriver .Chrome()
```python
browser     = webdriver.Chrome()
url_basica  = "http://www.sodimac.cl/sodimac-cl/category/cat710019/Tuercas"  
browser.get(url_basica)
```
#Correr Rutina
```python
   searchItemsSelenium.py
```
