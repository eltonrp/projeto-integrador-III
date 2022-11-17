from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Instancia driver e cria variáveis
def inicio():
  global driver
  driver = webdriver.Chrome('chromedriver.exe')
  url = 'https://descarte-inteligente.vercel.app/'
  driver.get(url)
  driver.maximize_window()
  sleep(2)

  # Campos para cadastrar
  global nome, cep, endereco, telefone
  nome = 'Nome Teste'
  cep = '13000000'
  endereco = 'Rua Aleatória, 202'
  telefone = '19000000000'

  # Move a tela até o campo de cadastro
  cadastro = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/h2')
  ActionChains(driver)\
    .move_to_element(cadastro)

  # Variáveis dos elementos de input e botão
  global input_name, input_cep, input_endereco, input_telefone, botao_cadastrar
  input_name = driver.find_element(By.XPATH, '//*[@id="name"]')
  input_cep = driver.find_element(By.XPATH, '//*[@id="cep"]')
  input_endereco = driver.find_element(By.XPATH, '//*[@id="address"]')
  input_telefone = driver.find_element(By.XPATH, '//*[@id="phone"]')
  botao_cadastrar = driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button')

# Fecha janela e finaliza o driver
def fim():
  driver.close()
  driver.quit()

# Função que cadastra vazio
def cadastra_vazio():
  try:
    qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  except:
    while qde_elementos == 0 or qde_elementos == None:
      sleep(1)
      qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  botao_cadastrar.click()
  sleep(3)
  nova_qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  passou = qde_elementos == nova_qde_elementos
  cabecalho = f'# Teste Cadastrar Vazio\n\
Quantidade de elementos iniciais = {qde_elementos}\n\
Quantidade final de elementos = {nova_qde_elementos}\n' 
  if passou:
    return cabecalho + 'Elemento nao cadastrado\nResultado = Passou no teste\n\n'
  return cabecalho + 'Elemento cadastrado\nResultado = Nao passou no teste\n\n'

# Função que cadastra todos os elementos
def cadastra_todos():
  try:
    qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  except:
    while qde_elementos == 0 or qde_elementos == None:
      sleep(1)
      qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  input_name.send_keys(nome)
  input_cep.send_keys(cep)
  input_endereco.send_keys(endereco)
  input_telefone.send_keys(telefone)
  botao_cadastrar.click()
  sleep(3)
  nova_qde_elementos = len(driver.find_elements(By.CLASS_NAME, 'item'))
  passou = qde_elementos != nova_qde_elementos
  cabecalho = f'# Teste Cadastrar Todos\n\
Quantidade de elementos iniciais = {qde_elementos}\n\
Quantidade final de elementos = {nova_qde_elementos}\n' 
  if not passou:
    return cabecalho + 'Elemento nao cadastrado\nResultado = Nao passou no teste\n'
  return cabecalho + 'Elemento cadastrado\nResultado = Passou no teste\n'

# Função que gera o arquivo de log
def gera_log():
  data = strftime("%d-%m-%y")
  hora = strftime("%H-%M-%S")
  with open(f'log-{data}-{hora}.txt', 'wt+') as arquivo:
    inicio()
    vazio = cadastra_vazio()
    print(vazio)
    arquivo.write(vazio)
    fim()
    inicio()
    todos = cadastra_todos()
    print(todos)
    arquivo.write(todos)
    fim()

gera_log()