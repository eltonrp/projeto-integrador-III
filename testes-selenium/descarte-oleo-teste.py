from time import sleep, strftime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://descarte-inteligente.vercel.app/'
driver.get(url)
driver.maximize_window()
sleep(5)

# Teste Cadastrar
nome = 'Nome Teste'
cep = '13000000'
endereco = 'Rua Aleatória, 202'
telefone = '19000000000'

cadastro = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/h2')

ActionChains(driver)\
  .move_to_element(cadastro)

# Variáveis dos elementos de input e botão
input_name = driver.find_element(By.XPATH, '//*[@id="name"]')
input_cep = driver.find_element(By.XPATH, '//*[@id="cep"]')
input_endereco = driver.find_element(By.XPATH, '//*[@id="address"]')
input_telefone = driver.find_element(By.XPATH, '//*[@id="phone"]')
botao_cadastrar = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button')

# Lista de elementos cadastrados
# lista_elementos = driver.find_elements(By.CLASS_NAME, 'item')

# Verificar se cadastra vazio
def cadastra_vazio():
  qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  print(qde_elementos)
  # input_name.send_keys(nome)
  # input_cep.send_keys(cep)
  # input_endereco.send_keys(endereco)
  botao_cadastrar.click()
  sleep(3)
  nova_qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  print(nova_qde_elementos)
  if qde_elementos == nova_qde_elementos:
      return f'Quantidade de elementos iniciais = {qde_elementos}\n\
Quantidade final de elementos = {nova_qde_elementos}\n\
Elemento nao cadastrado\n'
  else:
      return 'Cadastrou'

def gera_log():
  data = strftime("%d-%m-%y")
  hora = strftime("%H-%M-%S")
  arquivo = open(f'log-{data}-{hora}.txt', 'wt+')
  arquivo.write('# Teste Cadastrar Vazio\n')
  registro = cadastra_vazio()
  arquivo.write(registro)
  arquivo.close

gera_log()
        
driver.close()
driver.quit()
