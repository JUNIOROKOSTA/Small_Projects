from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import PyPDF2


# Pegar o Caminho para a pasta raiz do projeto(path_root)
ROOT_FOLDER = Path(__file__).parent

# montando o caminho para o chromedriver do selenium
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedrive' / 'chromedriver'


def chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


def init_clipchamp(useres, passwordes):
    sleep(3)
    browser.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/main/section/div/ul/li[1]/button/div').click()
    sleep(2)
    browser.find_element(
        By.XPATH, '//*[@id="i0116"]').send_keys(useres, Keys.ENTER)
    sleep(2)
    browser.find_element(
        By.XPATH, '//*[@id="i0118"]').send_keys(passwordes, Keys.ENTER)
    sleep(2)
    browser.find_element(
        By.XPATH, '//*[@id="idSIButton9"]').click()
    sleep(2)
    try:
        browser.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/main/section/div/ul/li[1]/button/div').click()
    except Exception as e:
        print(e)

    return f'OK...'


def open_clipchamp():
    sleep(7)
    browser.find_element(
        By.XPATH, '//*[@id="root"]/div/div[1]/div/nav/div/div[2]/div[4]/button/div/div[2]').click()
    sleep(3)
    browser.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/main/section/div/div/div/div/div/div/div/div/div[2]').click()


    return f'OK...'


def change_clipchamp(texto):
    sleep(3)
    browser.find_element(
        By.XPATH, '//*[@id="sidebar-button-recordCreate"]').click()
    sleep(3)
    browser.find_element(By.XPATH, '//*[@id="voiceover"]/div').click()
    sleep(3)
    browser.find_element(By.CSS_SELECTOR, f'body > div.Transition__'
                         f'TransitionContainer-sc-1hm06hn-0.kGqRtt.Dialog__'
                         f'Container-sc-graax7-0.fujfGT > div > div > div.VoiceOverForm__'
                         f'Container-sc-pqnjsb-0.fbITYF > div > div.VoiceOverForm__'
                         f'TextContainer-sc-pqnjsb-4.jKCwvT > textarea').send_keys(texto)
    sleep(3)
    browser.find_element(
        By.CSS_SELECTOR, f'body > div.Transition__TransitionContainer-sc-1hm06hn-0'
        f'.kGqRtt.Dialog__Container-sc-graax7-0.fujfGT > div > div > div.'
        f'VoiceOverForm__Container-sc-pqnjsb-0.fbITYF > div > button').click()


if __name__ == '__main__':
    useres = input("Digite seu email Hotmail: ")
    passwordes = input("Digite sua senha do email Hotmail: ")

    options = ('--disable-gpu', '--no-sandbox',)
    browser = chrome_browser(*options)
    browser.get(
        'https://app.clipchamp.com/login')
    print(init_clipchamp(useres, passwordes))

    print(open_clipchamp())

    caminho = Path(__file__).parent
    arquivo_pdf = caminho / 'pdf' / 'Overlord - Volume 01 - O Rei Undead.pdf'

    with open('texto.txt', 'a', encoding='utf-8') as f:
        texto = PyPDF2.PdfReader(arquivo_pdf)
        textos = []
        for i in range(5, 10):
            page = texto.pages[i]
            if len(page.extract_text()) > 100:
                valor = (str(page.extract_text().replace('OVERLORD         1 O Rei Undead',
                                                         ' ').replace('Capítulo          1 O Fim e o Começo', ' ')))

                textos.append(valor)
        for t in textos:
            f.write(t)
            change_clipchamp(t.replace('\n', ''))
            sleep(7)
            f.write('\n')

    sleep(5)

    browser.quit()
