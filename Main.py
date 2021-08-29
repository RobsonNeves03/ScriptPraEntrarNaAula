import selenium
from selenium import webdriver
import datetime
import mouse
import time
from pynput.mouse import Button, Controller
import schedule

def EntrarAula():
    mouse1 = Controller()

    #pega o driver e acessa o sistema
    driver = webdriver.Firefox()
    driver.get('https://cmspweb.ip.tv/')

    #clica em "Acesso para alunos"
    button1 = driver.find_element_by_id('access-student')
    button1.click()

    #realiza o login
    #detecta os campos a ser preenchidos
    field1 = driver.find_element_by_id('ra-student')
    field2 = driver.find_element_by_id('digit-student')
    field3 = driver.find_element_by_id('password-student')
    button2 = driver.find_element_by_id('btn-login-student')

    #coloca as informações nos campos correspondentes e clica em login
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


#Verifica o horário a cada minuto
data = datetime.datetime.now()
horario = data.strftime("%H%M")

def VerificaHorario():
    if(datetime.datetime.today().weekday() == 5):
        if(data.strftime("%H%M") == "2101"):
            EntrarAula()
        else:
            print("Not yet")

schedule.every(1).minutes.do(VerificaHorario)

while True:
    schedule.run_pending()
    time.sleep(60)
    data = datetime.datetime.now()



#Ferramentas
#verifica a posição do mouse
#while(t < 1):
    #time.sleep(4)
    #print(mouse.get_position())


