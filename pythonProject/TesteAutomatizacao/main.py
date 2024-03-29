import random
import time
from datetime import datetime

import pyautogui
import pyperclip
import selenium
import undetected_chromedriver as uc
from pynput.mouse import Listener
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class Banco:
    def __init__(self, codigo, contribuinte, numeroConta, dv):
        self.Codigo = codigo
        self.Agencia = contribuinte
        self.NumeroConta = numeroConta
        self.DV = dv

class Pessoa:
    def __init__(self, nome, dataNascimento, contribuinte, cpf, categoriaSegurado):
        self.nome = nome
        self.dataNascimeto = dataNascimento
        self.contribuinte = contribuinte
        self.cpf = cpf
        self.categoriaSegurado = categoriaSegurado


class Restituicao:
    def __init__(self, dataCriacao, tipoDocumento, tipoCredito, nit, competenciaAno, competenciaMes, valorPedRestituicao):
        self.dataCriacao = dataCriacao
        self.tipoDocumento = tipoDocumento
        self.tipoCredito = tipoCredito
        self.nit = nit
        self.competenciaAno = competenciaAno
        self.competenciaMes = competenciaMes
        self.valorPedRestituicao = valorPedRestituicao


class ContribuicoesDescontadas:
    def __init__(self, competencia, cnpj, entidadeBeneficente, remuneracaoRecebida, valorDescontado, nomeEmpresa):
        self.competencia = competencia
        self.cnpj = cnpj
        self.entidadeBeneficente = entidadeBeneficente
        self.remuneracaoRecebida = remuneracaoRecebida
        self.valorDescontado = valorDescontado
        self.nomeEmpresa = nomeEmpresa

def on_move(x, y):
    print('Mouse moved to ({}, {})'.format(x, y))

def CalculandoPosicaoAno(anoDocumento):
    anoDocumento = int(anoDocumento)
    anoAtual = datetime.now().year
    anoEscolhido = anoAtual - anoDocumento
    return 695 + anoEscolhido * 20

def CalculandoPosicaoMes(mesDocumento):
    mesDocumento = int(mesDocumento)
    return 695 + mesDocumento * 20

def CalculandoCategoriaSegurado(categoria):
    match(categoria):
        case "Empregado": 
            valor = 1
        case "Contribuinte Individual":
            valor = 3
        case "Trabalhador Avulso":
            valor = 5
        case _:
            print(f"A categoria era: {categoria}")
    return 888 + valor * 17

def CalculandoEntidadeBeneficente(beneficente):
    match(beneficente):
        case "Não":
            return 371
        case "Sim":
            return 296

def move_mouse_relative(x_rel, y_rel, duration=0.2):
    largura_tela, altura_tela = pyautogui.size()
    x = x_rel / 1920
    y = y_rel / 1080
    x_abs = int(x * largura_tela)
    y_abs = int(y * altura_tela)
    pyautogui.moveTo(x_abs, y_abs, duration=duration)

cpfUser = input("Digite o cpf do usuário nesse formato '000.000.000-00': ").strip()

print("Caso deseje pular essa etapa, apenas aperte enter.\n")
arm = input("Agora digite o código do banco: ").strip()
if(arm != ""):
    conta = Banco(arm, arm, arm, arm, arm)
    arm = input("Agora digite a agência: ").strip()
    conta.Agencia = arm
    arm = input("Agora digite o número da conta: ").strip()
    conta.NumeroConta = arm
    arm = input("Agora digite o DV: ").strip()
    conta.DV = arm

driver = uc.Chrome()
driver.get('https://conta.e-auditoria.com.br/Login')

cpf_field = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'styles__ButtonLogin-sc-12061y-3'))
)
cpf_field.click()

cpf_field = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.ID, 'username'))
)
cpf_field.send_keys("janeiro19@hotmail.com")

senha_field = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.ID, 'password'))
)
senha_field.send_keys("=Cbp2023")

driver.find_element(By.ID, "kc-login").click()

driver.maximize_window()
move_mouse_relative(1729, 358)
time.sleep(1)
pyautogui.click()

# buttons = driver.find_elements(By.CSS_SELECTOR, ".btn-success")
# button = buttons[4]
# button.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div.styles__Container-sc-ozds3h-0.dqLiUE'))
)

buttons = driver.find_elements(By.XPATH, '//div[@class="styles__Container-sc-ozds3h-0 dqLiUE"]')
button = buttons[1]
button.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary.ant-btn-lg"))
)

buttons = driver.find_elements(By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary.ant-btn-lg")
button = buttons[1]
button.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button.ant-btn.ant-btn-link.ant-btn-lg.ant-btn-icon-only"))
)
elemento.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.XPATH, f"//span[text()='{cpfUser}']"))
)

elemento_externo = driver.find_element(By.XPATH, f"//span[text()='{cpfUser}']/ancestor::div[contains(@style, 'width: 100%; display: flex;')]")
elemento_externo = elemento_externo.find_element(By.XPATH, ".//button[@title='Editar segurado']")
elemento_externo.click()

modalEspera = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.ID, "modal-segurado"))
)

move_mouse_relative(595, 652)
time.sleep(1)
pyautogui.click()

move_mouse_relative(595, 715, duration=0.2)
time.sleep(1)
pyautogui.click()

move_mouse_relative(789, 652, duration=0.2)
time.sleep(0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
if(arm != ""):
    pyautogui.press('delete')
    pyautogui.typewrite(conta.Codigo, interval=0.02)
else:
    pyautogui.hotkey('ctrl', 'c')
    codigo = pyperclip.paste()

move_mouse_relative(960, 652, duration=0.2)
time.sleep(0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
if(arm != ""):
    pyautogui.press('delete')
    pyautogui.typewrite(conta.Agencia, interval=0.02)
else:
    pyautogui.hotkey('ctrl', 'c')
    agencia = pyperclip.paste()

move_mouse_relative(1130, 652, duration=0.2)
time.sleep(0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
if(arm != ""):
    pyautogui.press('delete')
    pyautogui.typewrite(conta.NumeroConta, interval=0.02)
else:
    pyautogui.hotkey('ctrl', 'c')
    numero = pyperclip.paste()

move_mouse_relative(1300, 652, duration=0.2)
time.sleep(0.2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
if(arm != ""):
    pyautogui.press('delete')
    pyautogui.typewrite(conta.DV, interval=0.02)
else:
    pyautogui.hotkey('ctrl', 'c')
    Dv = pyperclip.paste()

if(arm == ""):
    banco2 = Banco(codigo, agencia, numero, Dv)

move_mouse_relative(1384, 716, duration=0.2)
time.sleep(0.2)
pyautogui.click()

move_mouse_relative(37, 109, duration=0.2)
time.sleep(1)
pyautogui.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.XPATH, f"//span[text()='{cpfUser}']"))
)

elemento.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.ID, "simple-tab-3"))
)
elemento.click()

move_mouse_relative(1646, 915, duration=0.2)
time.sleep(1)
pyautogui.click()

move_mouse_relative(1646, 990, duration=0.2)
time.sleep(1)
pyautogui.click()

elemento = WebDriverWait(driver, 30).until(
    selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button[title="Visualizar espelho do PER/DCOMP"]'))
)

totalRestituicoes = driver.find_elements(By.CSS_SELECTOR, 'button[title="Visualizar espelho do PER/DCOMP"]')
print(len(totalRestituicoes))

driver.execute_script("window.open('https://cav.receita.fazenda.gov.br/autenticacao', '_blank');")

contagem = 0

for i in range(len(totalRestituicoes)):
    total = driver.find_elements(By.CSS_SELECTOR, 'button[title="Visualizar espelho do PER/DCOMP"]')
    total[contagem].click()

    elemento = WebDriverWait(driver, 30).until(
        selenium.webdriver.support.expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, "td.MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignLeft"))
    )

    element = driver.find_elements(By.CSS_SELECTOR, "td.MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignLeft")

    pessoa = Pessoa(element[7].text, element[8].text, element[1].text, element[2].text, element[12].text)
    restituicao = Restituicao(element[0].text, element[3].text, element[4].text, element[5].text, element[6].text,
                              element[7].text, element[14].text)

    restituicao.competenciaMes = restituicao.competenciaAno[-2:]
    restituicao.competenciaAno = restituicao.competenciaAno[:4]
 
    listaContribuicoes = []

    table_body = driver.find_elements(By.CLASS_NAME, "MuiTableBody-root")
    elementos_table = table_body[4].find_elements(By.CLASS_NAME, "MuiTableRow-root")

    for unit in elementos_table:
        dados = unit.find_elements(By.CLASS_NAME, "MuiTableCell-root")

        contribuicoesDescontadas = ContribuicoesDescontadas(dados[0].text, dados[1].text, dados[2].text, dados[3].text,
                                                            dados[4].text, dados[5].text)
        listaContribuicoes.append(contribuicoesDescontadas)

    novas_alcas = driver.window_handles
    nova_aba_handle = novas_alcas[-1]

    driver.switch_to.window(nova_aba_handle)
    
    time.sleep(2)
    
    if(contagem == 0):
    
        elemento = driver.find_element(By.XPATH, "//input[@type='image'][contains(@onclick, 'validarHcaptcha')]")
        elemento.click()
    
        elemento = WebDriverWait(driver, 30).until(
            selenium.webdriver.support.expected_conditions.visibility_of_element_located(
                (By.ID, "accountId"))
        )
        time.sleep(random.randint(1, 4))
    
        elemento.send_keys("914.899.973-34")
    
        element = driver.find_element(By.CLASS_NAME, "button-continuar").click()
    
        time.sleep(random.randint(4, 6))
    
        element = driver.find_element(By.ID, "password")
        element.send_keys("=Renovar1")
    
        element = driver.find_element(By.ID, "submit-button").click()

        time.sleep(random.randint(4, 6))
        
        elemento = driver.find_element(By.ID, "btnPerfil").click()
    
        element = driver.find_element(By.ID, "txtNIPapel1")
        element.send_keys(pessoa.cpf)
    
        time.sleep(random.randint(1, 4))
    
        element = driver.find_elements(By.CLASS_NAME, "submit")
        element[1].click()

        time.sleep(random.randint(4, 7))
        
        element = driver.find_element(By.ID, "btn263").click()
        
        time.sleep(random.randint(1, 3))
    
        driver.find_element(By.XPATH, "//*[text()='Acessar PER/DCOMP WEB']").click()
    
    time.sleep(random.randint(4, 7))

    move_mouse_relative(724, 368, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(326, 458, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(341,526, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(465, 565, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(519, 599, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(481, 639, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(325, 668, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(1180, 532, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    DataAtual = datetime.today()
    pyautogui.typewrite(f"{pessoa.nome}//{DataAtual}", interval=0.02)

    move_mouse_relative(1853, 994, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(583, 709, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(992, 745, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(random.randint(4,6))

    move_mouse_relative(332, 673, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    
    alturaOpcao = CalculandoPosicaoAno(restituicao.competenciaAno)

    move_mouse_relative(332, alturaOpcao, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(622, 673, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    
    alturaOpcao = CalculandoPosicaoMes(restituicao.competenciaMes)

    move_mouse_relative(622, alturaOpcao, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(800, 673, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.typewrite(f"{restituicao.nit}", interval=0.02)

    move_mouse_relative(451, 868, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    
    alturaOpcao = CalculandoCategoriaSegurado(pessoa.categoriaSegurado)

    move_mouse_relative(451, alturaOpcao, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(950, 868, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()

    move_mouse_relative(950, 908, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(1860, 992, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    time.sleep(random.randint(4, 6))
    
    for cont in listaContribuicoes:

        move_mouse_relative(1755, 500, duration=0.2)
        time.sleep(1)
        pyautogui.click()
    
        time.sleep(random.randint(2, 4))

        move_mouse_relative(356, 670, duration=0.2)
        time.sleep(1)
        pyautogui.click()

        move_mouse_relative(356, 735, duration=0.2)
        time.sleep(0.2)
        pyautogui.click()
        pyautogui.typewrite(f"{cont.cnpj}", interval=0.02)
        
        posicao = CalculandoEntidadeBeneficente(cont.entidadeBeneficente)

        move_mouse_relative(posicao, 800, duration=0.2)
        time.sleep(1)
        pyautogui.click()

        move_mouse_relative(368, 850, duration=0.2)
        time.sleep(0.2)
        pyautogui.click()
        pyautogui.typewrite(f"{cont.remuneracaoRecebida}", interval=0.02)

        move_mouse_relative(990, 850, duration=0.2)
        time.sleep(0.2)
        pyautogui.click()
        pyautogui.typewrite(f"{cont.valorDescontado}", interval=0.02)

        move_mouse_relative(1526, 910, duration=0.2)
        time.sleep(1)
        pyautogui.click()

    move_mouse_relative(1850, 993, duration=0.2)
    time.sleep(1)
    pyautogui.click()
    
    time.sleep(random.randint(2, 4))

    move_mouse_relative(480, 523, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.typewrite(f"{restituicao.valorPedRestituicao}", interval=0.02)

    move_mouse_relative(1850, 993, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    time.sleep(random.randint(4, 6))

    move_mouse_relative(330, 667, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(330, 705, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(665, 667, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    if(arm != ""):
        pyautogui.typewrite(f"{conta.Codigo}", interval=0.02)
    else:
        pyautogui.typewrite(f"{banco2.Codigo}", interval=0.02)

    move_mouse_relative(330, 740, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    if(arm != ""):
        pyautogui.typewrite(f"{conta.Agencia}", interval=0.02)
    else:
        pyautogui.typewrite(f"{banco2.Agencia}", interval=0.02)

    move_mouse_relative(740, 740, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    if(arm != ""):
        pyautogui.typewrite(f"{conta.NumeroConta}", interval=0.02)
    else:
        pyautogui.typewrite(f"{banco2.NumeroConta}", interval=0.02)

    move_mouse_relative(960, 740, duration=0.2)
    time.sleep(0.2)
    pyautogui.click()
    if(arm != ""):
        pyautogui.typewrite(f"{conta.DV}", interval=0.02)
    else:
        pyautogui.typewrite(f"{banco2.DV}", interval=0.02)

    move_mouse_relative(1850, 995, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(1835, 995, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    move_mouse_relative(100, 300, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    driver.switch_to.window(driver.window_handles[0])

    move_mouse_relative(33, 116, duration=0.2)
    time.sleep(1)
    pyautogui.click()

    elemento = WebDriverWait(driver, 30).until(
        selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button[title="Visualizar espelho do PER/DCOMP"]'))
    )
    
    contagem = contagem + 1
    print(contagem)

    # with Listener(on_move=on_move) as listener:
    #     listener.join()
    # 

input("Pressione Enter para encerrar o programa...")
driver.quit()