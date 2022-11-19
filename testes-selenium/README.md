# Teste de Sistema com Selenium Webdriver

## Descrição dos testes aplicados
* Teste de Sistema com Selenium Webdriver

### Objetivo da aplicação
* Exibir pontos de coleta, assim como permitir cadastrar novos pontos e excluí-los.

### Funcionalidade da aplicação a ser analizada
* Cadastro de pontos de coleta.

### Objetivo do teste de software
* Atividade realizada para revelar defeitos existentes no software.

### Classificação do teste
* Nível
  * Sistema
* Tipo
  * Funcionalidade
* Técnica
  * Teste Funcional

### Finalidade e características do teste de sistema
* apontar falhas em aspectos gerais do sistema
* encontrar falhas que o usuário final pode ter acesso
* são testes avaliados do ponto de vista do usuário
* avalia a funcionalidade geral do programa

### Objetivo específico do teste a ser aplicado
* avaliar a principal funcionalidade da aplicação: 
  * cadastrar pontos de coleta
### Metodologia
Objetivando eliminar erros cadastrais, foi gerado um script na linguagem Python, utilizando a ferramenta Selenium, em que serão analizadas as seguintes hipóteses:

* Cadastrar todos campos normalmente (controle)
  * Esperado = cadastrar
* Cadastrar todos campos vazios
  * Esperado = não cadastrar
* Cadastrar qualquer campo obrigatório vazio
  * Esperado = não cadastrar
* Cadastrar todos os campos obrigatórios, exceto o campo não obrigatório (telefone)
  * Esperado = cadastrar
* Cadastrar campos numéricos (cep e telefone) com quaisquer outros caracteres
  * Esperado = não cadastrar
