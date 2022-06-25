import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'

with webdriver.Chrome() as b:
    b.get(url)
    
#   ����� ��� ����� � ������ � �������� � ������
    numb_list = [int(i.text) for i in 
                 b.find_elements_by_css_selector('h2 .nowrap') 
                 if i.text.isdecimal()]
    
#   �������� ����������� ������
    select = Select(b.find_element_by_tag_name('select'))
    
#   ����� ������ � ������
    select.select_by_value(f'{sum(numb_list)}')
    
#   ����� ������ � �� �������
    b.find_element_by_class_name('btn').click()
    
#   �������� ������ � ��������� �� ���� ������
    print(b.switch_to.alert.text.split()[-1])