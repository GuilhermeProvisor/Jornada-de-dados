from selenium import webdriver #Simulação de um browser
from selenium.common.exceptions import TimeoutException
from time import sleep #Simulação do tempo de carregamento

#Precisamos definir qual driver vamos utilizar
driver = webdriver.Firefox()

#Define um timeout implícito
driver.set_page_load_timeout(5)

#Vamos fazer uma tratativa de try-except de entrar na nossa página
try:
    driver.get("http://localhost:8501") #A aplicação ta nessa porta, testa se ela está online
    sleep(5) #Esperar 5 segundos
    print("Acessou a página com sucesso")
except TimeoutException: #Se não funcionou...
    print("Tempo de carregamento da página excedeu o limite.")
finally:
    driver.quit()
