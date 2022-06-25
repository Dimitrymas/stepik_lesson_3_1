import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'

with webdriver.Chrome() as b:
    b.get(url)
    
#   Ќайти все цыфры в строке и добавить в список
    numb_list = [int(i.text) for i in 
                 b.find_elements_by_css_selector('h2 .nowrap') 
                 if i.text.isdecimal()]
    
#   открытие выпадающего списка
    select = Select(b.find_element_by_tag_name('select'))
    
#   поиск ответа в списке
    select.select_by_value(f'{sum(numb_list)}')
    
#   поиск кнопки и ее нажатие
    b.find_element_by_class_name('btn').click()
    
#   ожидание алерта и получение из него ответа
    print(b.switch_to.alert.text.split()[-1])