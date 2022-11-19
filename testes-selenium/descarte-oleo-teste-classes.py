from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from random import sample, randint, randrange
from selenium.webdriver.common.keys import Keys

class TesteCadastro:
  # Método inicia driver, variáveis e elementos da página
  def iniciar(self):
    # Inicia variáveis de cadastro
    self.nome = sample(['Coleta do Sul', 'Gordura Doce', 'Cheiro do Ralo', 'Óleo Puro'], 1)
    self.cep = str('130') + str(randrange(10, 90, 10)) + '0' + str(randrange(10, 90, 10))
    self.endereco = sample(['Rua Azul, 222', 'Rua X, 56', 'Rua Branca, 78', 'Rua das Pomba, 900'], 1)
    self.telefone = randint(11999999999, 19999999999)
    # Inicia driver
    self.driver = webdriver.Chrome('chromedriver.exe')
    self.url = 'https://descarte-inteligente.vercel.app/'
    self.driver.get(self.url)
    self.driver.maximize_window()
    sleep(3)
    # Variáveis dos elementos de input e botão
    self.input_name = self.driver.find_element(By.XPATH, '//*[@id="name"]')
    self.input_cep = self.driver.find_element(By.XPATH, '//*[@id="cep"]')
    self.input_endereco = self.driver.find_element(By.XPATH, '//*[@id="address"]')
    self.input_telefone = self.driver.find_element(By.XPATH, '//*[@id="phone"]')
    self.botao_cadastrar = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button')
  
  # Método para fechar sessão e encerrar driver
  def fechar(self):
    self.driver.close()
    self.driver.quit()

  # Método mover tela até área de cadastro
  def mover_tela(self):
    self.cadastro = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/h2')
    ActionChains(self.driver)\
      .move_to_element(self.cadastro)

  # Método que cadastra vazio
  def cadastra_vazio(self):
    try:
      qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    except:
      while qde_elementos == 0 or qde_elementos == None:
        sleep(1)
        qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    self.botao_cadastrar.click()
    sleep(3)
    nova_qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    passou = qde_elementos == nova_qde_elementos
    cabecalho = f'# Teste Cadastrar Vazio\n\
\tQuantidade de elementos iniciais = {qde_elementos}\n\
\tQuantidade final de elementos = {nova_qde_elementos}\n\
\tEsperado = Nao cadastrar\n' 
    if passou:
      return cabecalho + '\tElemento nao cadastrado\n\tResultado = Passou no teste\n\n'
    return cabecalho + '\tElemento cadastrado\n\tResultado = Nao passou no teste\n\n'

  # Método que cadastra todos os elementos
  def cadastra_todos(self):
    try:
      qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    except:
      while qde_elementos == 0 or qde_elementos == None:
        sleep(1)
        qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    self.input_name.send_keys(self.nome)
    self.input_cep.send_keys(self.cep)
    self.input_cep.send_keys(Keys.TAB)
    sleep(2)
    # input_endereco.send_keys(endereco)
    self.input_telefone.send_keys(self.telefone)
    self.botao_cadastrar.click()
    sleep(3)
    nova_qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    passou = qde_elementos != nova_qde_elementos
    cabecalho = f'# Teste Cadastrar Todos\n\
\tQuantidade de elementos iniciais = {qde_elementos}\n\
\tQuantidade final de elementos = {nova_qde_elementos}\n\
\tEsperado = Cadastrar\n' 
    if not passou:
      return cabecalho + '\tElemento nao cadastrado\n\tResultado = Nao passou no teste\n\n'
    return cabecalho + '\tElemento cadastrado\n\tResultado = Passou no teste\n\n'

  # Método que tenta cadastrar com um campo obrigatório vazio aleatoriamente
  def cadastra_um_vazio(self):
    try:
      qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    except:
      while qde_elementos == 0 or qde_elementos == None:
        sleep(1)
        qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    lista_itens_obrigatorios = [self.input_name, self.input_cep, self.input_endereco]
    lista_sorteada = sample(lista_itens_obrigatorios, 2)
    if self.input_cep in lista_sorteada:
      self.input_cep.send_keys(self.cep)
      self.input_cep.send_keys(Keys.TAB)
      sleep(2)
    else:
      for itens in lista_sorteada:
        if itens == self.input_name:
          itens = self.input_name.send_keys(self.nome)
        # if itens == input_cep:
        #   itens = input_cep.send_keys(cep)
        #   input_cep.send_keys(Keys.TAB)
        #   sleep(2)
        if itens == self.input_endereco:
          itens = self.input_endereco.send_keys(self.endereco)
    self.botao_cadastrar.click()
    sleep(3)
    nova_qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    passou = qde_elementos == nova_qde_elementos
    cabecalho = f'# Teste Cadastrar um Obrigatorio Vazio\n\
\tQuantidade de elementos iniciais = {qde_elementos}\n\
\tQuantidade final de elementos = {nova_qde_elementos}\n\
\tEsperado = Nao cadastrar\n' 
    if passou:
      return cabecalho + '\tElemento nao cadastrado\n\tResultado = Passou no teste\n\n'
    return cabecalho + '\tElemento cadastrado\n\tResultado = Nao passou no teste\n\n'

  # Método cadastra campos numéricos (cep e telefone) com outros caracteres
  def cadastra_numericos(self):
    try:
      qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    except:
      while qde_elementos == 0 or qde_elementos == None:
        sleep(1)
        qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    self.input_name.send_keys(self.nome)
    self.input_cep.send_keys('Teste')
    self.input_cep.send_keys(Keys.TAB)
    sleep(2)
    # input_endereco.send_keys(endereco)
    self.input_telefone.send_keys('Outro teste')
    self.botao_cadastrar.click()
    sleep(3)
    nova_qde_elementos = len(self.driver.find_elements(By.CLASS_NAME, 'item'))
    passou = qde_elementos == nova_qde_elementos
    cabecalho = f'# Teste Cadastrar Numericos\n\
\tQuantidade de elementos iniciais = {qde_elementos}\n\
\tQuantidade final de elementos = {nova_qde_elementos}\n\
\tEsperado = Nao cadastrar\n' 
    if passou:
      return cabecalho + '\tElemento nao cadastrado\n\tResultado = Passou no teste\n\n'
    return cabecalho + '\tElemento cadastrado\n\tResultado = Nao passou no teste\n\n'

  # Método que chama todos os métodos e gera arquivo de log
  def gera_log(self):
    data = strftime("%d-%m-%y")
    hora = strftime("%H-%M-%S")
    with open(f'log-{data}-{hora}.txt', 'wt+') as arquivo:
      self.iniciar()
      self.mover_tela()
      vazio = self.cadastra_vazio()
      print(vazio)
      arquivo.write(vazio)
      self.fechar()
      self.iniciar()
      self.mover_tela()
      todos = self.cadastra_todos()
      print(todos)
      arquivo.write(todos)
      self.fechar()
      self.iniciar()
      self.mover_tela()
      um_vazio = self.cadastra_um_vazio()
      print(um_vazio)
      arquivo.write(um_vazio)
      self.fechar()
      self.iniciar()
      self.mover_tela()
      numericos = self.cadastra_numericos()
      print(numericos)
      arquivo.write(numericos)
      self.fechar()
  
teste = TesteCadastro()
teste.gera_log()
