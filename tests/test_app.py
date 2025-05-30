from selenium import webdriver #Simulação de um browser
from selenium.common.exceptions import TimeoutException
from time import sleep #Simulação do tempo de carregamento

import pytest
import subprocess

@pytest.fixture #Código que vai ser chamado para todos os testes
def driver():
    #Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    #Iniciar o WebDriver usando o GeckoDriver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver #Roda varias vezes

    #Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    #Verificar se a página abre
    driver.get("https://localhost:8501")
    sleep(5)