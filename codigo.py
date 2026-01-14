import pyautogui
import time

#a cada comando ele vai aguardar meio sec para não bugar o codigo a ser executado
pyautogui.PAUSE = 0.5

#passo 1: Abrir sistema da empresa

#abrir o navegador
#apertar tecla Windows
pyautogui.press("win")

#digitar texto "Opera"
pyautogui.write("chrome")

#apertar tecla enter
pyautogui.press("enter")

#digitar o link da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

#apertar tecla enter
pyautogui.press("enter")
time.sleep(3)

#passo 2: fazer login
pyautogui.click(x=600, y=506)
pyautogui.write("") #cadastrar o email do login
pyautogui.press("tab") #trocar do espaço do email para o espaço do login
pyautogui.write("") #inserir a senha utilizada
pyautogui.press("tab")
pyautogui.press("enter") #entrar no site com os dados cadastrados

#Passo 3: Importar a base de dados dos produtos

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

#Passo 4: Cadastrar primeiro produto

for linha in tabela.index:

    pyautogui.click(x=599, y=360) #clica no primeiro ponto
    pyautogui.press("tab")
    codigo = tabela.loc[linha,"codigo"] #busca o codigo do produto na tabela
    pyautogui.write(str(codigo))#insere o código na tabela do site
    pyautogui.press("tab")
    marca = tabela.loc[linha,"marca"]#busca a marca do produto na tabela
    pyautogui.write(str(marca))#insere a marca na tabela do site
    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]#busca o tipo do produto na tabela
    pyautogui.write(str(tipo))#insere o tipo na tabela do site
    pyautogui.press("tab")
    categoria = tabela.loc[linha,"categoria"]#busca a categoria do produto na tabela
    pyautogui.write(str(categoria))#insere a categoria na tabela do site
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha,"preco_unitario"]#busca o preço unitario do produto na tabela
    pyautogui.write(str(preco_unitario))#insere o preço unitário na tabela do site
    pyautogui.press("tab")
    custo = tabela.loc[linha,"custo"] #busca o custo do produto na tabela
    pyautogui.write(str(custo))#insere o custo na tabela do site
    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]#busca a observação do produto na tabela
    if obs != "nan": #verifica se possui ou não observação
        pyautogui.write(obs)#insere a observação na tabela do site
    pyautogui.press("tab")
    pyautogui.press("enter") #depois de inserir os dados necessários, ele envia os dados para a tabela no site


    pyautogui.press("home") #ele voltar para o início da pagina e inserir os próximos dados

