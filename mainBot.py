from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import random
import os 

''' Coloque entre as aspas em "arq" o caminho do arquivo de texto com os usuarios (.txt)'''
arq = "Insira_aqui"
#by @aveusalex 

def remove_repetidos(diretorio):
    l = []
    f = open(diretorio, "r")
    A = f.read()
    A = A.split("!")
    for i in A:
       if i not in l:
            l.append(i)
    return l

def digite_como_pessoa(frase, onde_digitar):
    for letra in frase:
        onde_digitar.send_keys(letra)
        time.sleep(random.randint(1, 5) / 15)


def main(usuario, pasword, qts_comments, pessoas_por_comment, link, frase_antes, desligar_apos_finalizacao):
    n = 0
    contagem = 0
    qtsjafoi = 0
    A = []
    sair = False
    #Onde iniciar a lista?
    o = 40
    er = 0
    #by @aveusalex
    #insira a base de dados em useerss
    comentarios = remove_repetidos(arq)
    
    ''' Insira em "webdriver.Firefox("")" o caminho do geckodriver, entre as aspas '''
    
    driver = webdriver.Firefox(executable_path= "Insira_Aqui")
    driver.get(link)
    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='username']").click()
    login = driver.find_element_by_xpath("//input[@name='username']")
    login.clear()
    #usuario de login
    digite_como_pessoa(usuario, login)
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='password']").click()
    senha = driver.find_element_by_xpath("//input[@name='password']")
    senha.clear()
    #senha de login
    digite_como_pessoa(pasword, senha)
    time.sleep(2)
    senha.send_keys(Keys.RETURN)
    time.sleep(6)
    try:
        driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        time.sleep(3)
    except: 
        pass
    
    while sair == False:
        try:
            for i in range(qts_comments):
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                campo_comentario.clear()
                time.sleep(5)
                                        
                while contagem != pessoas_por_comment:
                    A.append(comentarios[o] + " ")
                    contagem += 1
                    o += 1
                    if o == len(comentarios):
                        o = 0
                contagem = 0
                               
                digite_como_pessoa(frase_antes, campo_comentario)
                time.sleep(random.randint(2, 4))

                for w in range(0, pessoas_por_comment):
                    digite_como_pessoa(A[w], campo_comentario)
                    time.sleep(random.randint(4, 5))
                time.sleep(random.randint(4, 5))
                campo_comentario.send_keys(Keys.RETURN)
                time.sleep(random.randint(50, 55))
                A.clear()
                qtsjafoi += 1
                print(qtsjafoi)
                er = 0
                if qtsjafoi == qts_comments:
                    sair = True
                
        except:
            print("Error")
            er += 1
            time.sleep(10)
            if er == 3:
                sair = True
    
    if desligar_apos_finalizacao == 1:
        os.system('shutdown -s')

def contar(base_dados):
    a = base_dados.split("!")
    print(len(a))
    #by @aveusalex

f = open(arq, "r")
contar(f.read())

if __name__ == "__main__":
    print("Por Aveusalex, @aveusalex")
    main("Seu usuario", "Sua senha", Quantidade de comentarios, Pessoas marcadas por comentario, "Link do sorteio", "Frase antes(deixar vazio caso não haja, só as aspas)", desligar após fim (0 ou 1))
    
