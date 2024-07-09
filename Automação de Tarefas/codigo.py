# passo 1 - Entar no sistema da Empresa
    # link:https://dlp.hashtagtreinamentos.com/python/intensivao/login

# passo 2 - Fazer Login

# passo 3 - Pegar base de dados

# passo 4 - Cadastrar um Produto

# passo 5 - Repetir o passo 4 até cdastrar todos os produtos

import pyautogui
import time

#pyautogui.click - clicar com o Mouse
#pyautogui.write - Escrever  um Texto
#pyautogui.press - Apertar 1 tecla
#pyautogui.hotkey - combinações de teclas 
#pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 1
# passo 1 - Entar no sistema da Empresa
#Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# link:https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# passo 2 - Fazer Login
pyautogui.click(x=501, y=404)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("bomfimrobson90@gmail.com")

#passar para o campo de senha 
pyautogui.press("tab")
pyautogui.write("rafael2014")

pyautogui.click(x=673, y=565)

time.sleep(3)

# passo 3 - Pegar base de dados
import pandas as pd

produtos = pd.read_csv("produtos.csv")
print(produtos)

# passo 4 - Cadastrar um Produto
for linha in produtos.index:
    #código

    pyautogui.click(x=490, y=295)
    codigo = str(produtos.loc[linha, "codigo"])
    pyautogui.write(codigo)
    #marca
    pyautogui.press("tab")
    marca = str(produtos.loc[linha, "marca"])
    pyautogui.write(marca)
    #tipo
    pyautogui.press("tab")
    tipo = str(produtos.loc[linha, "tipo"])
    pyautogui.write(tipo)
    #categoria
    pyautogui.press("tab")
    categoria = str(produtos.loc[linha, "categoria"])
    pyautogui.write(categoria)
    #cresc_unitario
    pyautogui.press("tab")
    preco_unitario = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    #custo
    pyautogui.press("tab")
    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)
    #obs
    pyautogui.press("tab")
    obs = str(produtos.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    #clicar no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# passo 5 - Repetir o passo 4 até cdastrar todos os produtos
