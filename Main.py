import selenium
from selenium import webdriver
import datetime
import mouse
import time
from pynput.mouse import Button, Controller

def aula():
    mouse1 = Controller()

    #pega o driver e acessa o sistema
    driver = webdriver.Firefox()
    driver.get('https://cmspweb.ip.tv/')

    #clica em "Acesso para alunos"
    button1 = driver.find_element_by_id('access-student')
    print("Botão: ", button1.get_attribute('innerHTML'))
    button1.click()

    #realiza o login
    #detecta os campos a ser preenchidos
    field1 = driver.find_element_by_id('ra-student')
    field2 = driver.find_element_by_id('digit-student')
    field3 = driver.find_element_by_id('password-student')
    button2 = driver.find_element_by_id('btn-login-student')

    #coloca a/s informações nos campos correspondentes e clica em login
    field1.send_keys("000110121115")
    field2.send_keys("5")
    field3.send_keys("7fmdfa0h")
    button2.click()

    #entra na aula
    time.sleep(8)
    mouse.move(2441, 138, absolute=True, duration=1)
    mouse1.press(Button.left)
    mouse1.release(Button.left)
    time.sleep(2)
    mouse.move(2228, 232, absolute=True, duration=1)
    mouse1.press(Button.left)
    mouse1.release(Button.left)


#data = datetime.datetime.now()
aula()
#while(t < 1):
    #time.sleep(4)
    #print(mouse.get_position())

#print(data.strftime("%H%M"))