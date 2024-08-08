import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from userdata import LOGIN, SENHA

def open_browser():
    """Abre o Browser customizado (CentBrowser) com uso do chromedriver (Selenium)"""
    path_chromedriver = r"C:\Users\med-pediatria\Desktop\ale\chromedriver.exe"
    path_centbrowser = r"C:\CentBrowser\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = path_centbrowser
    # Argumento necessário para não perder os dados do usuário toda vez que abrir o browser
    chrome_options.add_argument(r"user-data-dir=C:\CentBrowser\User Data")

    service = Service(executable_path=path_chromedriver)
    driver = webdriver.Chrome(options=chrome_options, service=service)

    return driver

def pedir_dietas(driver, qtd_patients, login, senha):
    # Maximizar tela e entrar na página inicial de interesse
    driver.maximize_window()
    driver.get("http://143.106.246.32:8020/mvpep/index_appletless.html?t=1706723763696#")
    time.sleep(20)

    # Fazer login
    # Clica no campo login
    pyautogui.click(1025, 403)
    pyautogui.typewrite(login)
    time.sleep(5)
    # Clica no campo senha
    pyautogui.click(1025, 429)
    pyautogui.typewrite(senha)
    time.sleep(1)
    # Faz login1
    pyautogui.press('enter')

    # Entrar na aba 'Internações'
    time.sleep(5)
    pyautogui.click(71, 708)
    time.sleep(5)

    # Acessar cada página de paciente e fazer o pedido
    y_position = 290
    cliques_pra_baixo = 0
    for i, patient in enumerate(range(qtd_patients)):
        # Este trecho é para o caso de ser necessário um scroll down
        if i >= 13:
            cliques_pra_baixo += 1
            # Clica na seta para baixo
            for i in range(cliques_pra_baixo):
                pyautogui.click(1344, 671)
            # A posição y, nesse caso, é fixa, já que é sempre a última da tela
            y_position = 658
        # Entra na tela do usuário
        pyautogui.click(155, y_position)
        time.sleep(5)
        # Se o paciente tem registro anterior, clica no copiar e assinar o pedido
        pyautogui.click(297, 665)
        time.sleep(2)
        pyautogui.click(346, 665)
        time.sleep(5)

        # Se o paciente não possui registro anterior, lança um novo pedido de acompanhante do tipo dieta geral,
        # em seguida salva e assina
        pyautogui.click(800, 306)
        time.sleep(1)
        pyautogui.click(800, 355)
        time.sleep(1)
        pyautogui.click(244, 410)
        time.sleep(1)
        pyautogui.typewrite('12373')
        time.sleep(1)
        pyautogui.click(240, 431)
        time.sleep(1)
        pyautogui.click(260, 671)
        time.sleep(5)
        pyautogui.click(346, 665)
        time.sleep(2)
        pyautogui.click(61, 201)
        time.sleep(5)

        # Acréscimo de posição para o próximo paciente da lista (se não for por scroll down)
        y_position += 30

    time.sleep(10)

print("Bem vindo ao programa de lançamento automático de dietas!")
qtd_patients = int(input("Insira a quantidade de pacientes: "))
driver = open_browser()
pedir_dietas(driver, qtd_patients, LOGIN, SENHA)
