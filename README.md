# Elite Pointers
### Este repositório é destinado ao projeto de capacitação da Altotech juniors, onde decidimos construir um e-commerce destinado a venda de relógios
### Para realiza-lo utilizamos Html, Css e Js na parte do front-end e o framework django utilizando python para desenvolver o back-end
## Configurando ambiente
### Para instalar as dependências e rodar a aplicação siga os seguintes passos:
### Para criar um ambiente virtual:
```python
python -m venv (nome da venv, sem os parenteses)
``` 
### Para ativar a venv(windows, mantenha ativada):
```python
(nome da venv, sem os parenteses)/Scripts/activate
``` 
### Para instalar as dependências:
```python
pip install -r requirements.txt
``` 
### Crie o arquivo **`.env`**(na fonte do projeto) e insira esse trecho de código e suas informações onde informado:
```python
EMAIL_HOST_USER = 'seu email aqui'
EMAIL_HOST_PASSWORD = 'sua senha aqui'
EMAIL_HOST = 'o server do seu email aqui' (caso não saiba basta pesquisar no google server smtp e seu host, como por exemplo smtp server gmail)
```
### Abra o terminal e digite o seguinte comando:
```python
python manage.py migrate
```
### Agora, ainda no terminal, para rodar a aplicação digite:
```python
python manage.py runserver
```
### Se você seguiu os passos corretamente, agora a aplicação está rodando, para visualizar a página basta usar **`crtl + botão esquerdo`** no link que apareceu no terminal
### Caso sua venv desative e você queira ativar ela de novo basta usar o mesmo comando de ativiação e rodar novamente a aplicação
