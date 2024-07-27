import pyautogui as pg
import time
import pandas as pd
#abrindo navegador / opening navegator

pg.press('win')
time.sleep(1)
pg.write('google chrome')
pg.press('enter')
time.sleep(2)
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(2)
pg.press('enter')
time.sleep(2)

#login
#print(pyautogui.position()) /  finding the location to move the mouse 
pg.moveTo(485,425)
time.sleep(1)
pg.click()
pg.write('ababi@gmail.com')
time.sleep(1)
pg.press('tab')
pg.write('lababage')
pg.press('enter')

#cadastro / sign up 
time.sleep(2)
tabela = pd.read_csv('automacao/produtos.csv')

for linha in tabela.index: #index = linha  columns = colunas
    pg.moveTo(572,309)
    time.sleep(2)
    pg.click()
    codigo = str(tabela.loc[linha, 'codigo'])
    pg.write(codigo)

    time.sleep(1)
    pg.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pg.write(marca)
    pg.press('tab')

    tipo= str(tabela.loc[linha, 'tipo'])
    pg.write(tipo)
    time.sleep(1)
    pg.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pg.write(categoria)
    time.sleep(1)
    pg.press('tab')

    preco = str(tabela.loc[linha, 'preco_unitario'])
    pg.write(preco)
    time.sleep(1)
    pg.press('tab')

    custo= str(tabela.loc[linha, 'custo'])
    pg.write(custo)
    time.sleep(1)
    pg.press('tab')


    obs = str(tabela.loc[linha, 'obs'])
    pg.write(obs)
    time.sleep(1)
    

    time.sleep(1)
    pg.moveTo(582,578)
    pg.click()
    pg.click()

    time.sleep(1)
    pg.scroll(1000)
    time.sleep(1)




