# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #usado para selecionar elementos
from selenium.webdriver.common.keys import Keys #usado para importar teclas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #espera para encontrar elemento

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located( #esperar que o elemento esteja na tela
            (By.NAME, 'q') #localiza elemento de nome q
        )
    )
    search_input.send_keys('Hello World!') #LOCALIZA O INPUT E ADICIONA (digita) 'Hello World' na pesquisa
    search_input.send_keys(Keys.ENTER) #PRESSIONA ENTER

    results = browser.find_element(By.ID, 'search') # seleciona os elementos do id search
    links = results.find_elements(By.TAG_NAME, 'a') # seleciona os elementos de results com tag name 'a'
    links[0].click() #clicar no primeiro link


    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)