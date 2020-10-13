from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date
from pytz import timezone
import time
import random


# Insira dentro das aspas de arq o diretorio da base de dados.
arq = "C:\\Users\\TaniaMaraEcheverria\\Desktop\\lista.txt"

# Insira dentro das aspas de usuario o username da conta que vai enviar as propagandas (pode usar essa do exemplo)
usuario = "edymarareges"

# Insira dentro das aspas de senha a senha da conta anterior.
senha = ""

# Insira o número de comentários a ser realizado.
qts_comments = 15

# Insira o número de pessoas por comentário.
pessoas_por_comment = 1

# Insira dentro das aspas de link o link do instagram. Já está aí.
link = "https://www.instagram.com/p/B9w1EU1Jel2/?igshid=1bljon9zyylz7"

# Insira se aleatorio ou não (False, True). Por padrão é False.
aleatorio = True

# Insira dentro das aspas de texto o texto que será escrito antes da marcação.
texto = ""

# Insira em relatorio o local que deseja salvar o relatório.
relatorio = "C:\\Users\\TaniaMaraEcheverria\\Desktop\\relatorioSorteios.txt"


def remove_repetidos(diretorio, aleatorio):
    lista_limpa = []

    with open(diretorio, "r") as baseNomes:
        listaSuja = baseNomes.read()
        listaSuja = listaSuja.split("!")

    for usuario in listaSuja:
        if usuario not in lista_limpa:
            lista_limpa.append(usuario)

    if aleatorio:
        random.shuffle(lista_limpa)

    print('Quantidade de users:', len(lista_limpa))

    return lista_limpa


def digite_como_pessoa(frase, onde_digitar):

    for letra in frase:
        onde_digitar.send_keys(letra)
        time.sleep(random.randint(1, 5) / 15)


def stopwatch(value):

    dias = int(value/(24*3600))

    valorH = value - (dias * 24 * 3600)
    horas = int(valorH / 3600)

    valorM = valorH - (horas * 3600)
    minutos = int(valorM / 60)

    valorS = valorM - (minutos * 60)
    segundos = int(valorS)

    return f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos."


def main(usuario, pasword, qts_comments, pessoas_por_comment, link, aleatorio=False, frase_antes=''):
    global qtsjafoi, ultimo_marcado, problemas
    problemas = 0
    continuarr = False
    tentativas = 0
    qtsjafoi = 0
    sair = False
    comentarios = remove_repetidos(arq, aleatorio)
    # Insira o diretorio do geckodriver:
    driver = webdriver.Firefox(executable_path= "C:\\Users\\TaniaMaraEcheverria\\Desktop\\as\\geckodriver.exe")
    driver.get(link)
    time.sleep(45)
    while not continuarr:
        try:
            driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]").click()
            time.sleep(5)
            continuarr = True
        except:
            time.sleep(10)
    continuarr = False

    while not continuarr:
        try:
            driver.find_element_by_xpath("//input[@name='username']").click()
            login = driver.find_element_by_xpath("//input[@name='username']")
            login.clear()
            digite_como_pessoa(usuario, login)
            continuarr = True
            time.sleep(3)
        except:
            time.sleep(10)
    continuarr = False

    while not continuarr:
        try:
            driver.find_element_by_xpath("//input[@name='password']").click()
            senha = driver.find_element_by_xpath("//input[@name='password']")
            senha.clear()
            digite_como_pessoa(pasword, senha)
            time.sleep(2)
            senha.send_keys(Keys.RETURN)
            continuarr = True
            time.sleep(6)
        except:
            time.sleep(10)

    for iteracao in range(2):
        try:
            driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
            time.sleep(3)
        except:
            pass

    c = len(comentarios)
    b = 0
    while not sair:
        try:
            continuar = True
            driver.find_element_by_class_name('Ypffh').click()
            campo_comentario = driver.find_element_by_class_name('Ypffh')
            campo_comentario.clear()

            a, b = b, b + pessoas_por_comment
            if b > c and a != 0:
                b -= c
                pessoas_no_comentario = comentarios[a:c] + comentarios[0:b]
            elif c < pessoas_por_comment:
                pessoas_no_comentario = comentarios * pessoas_por_comment
                b = 0
            else:
                pessoas_no_comentario = comentarios[a:b]

            digite_como_pessoa(frase_antes, campo_comentario)
            time.sleep(random.randint(2, 4))

            for w in range(0, pessoas_por_comment):
                digite_como_pessoa(pessoas_no_comentario[w] + ' ', campo_comentario)
                time.sleep(random.randint(4, 5))
                if w == pessoas_por_comment - 1:
                    ultimo_marcado = pessoas_no_comentario[w]

            time.sleep(random.randint(4, 5))
            campo_comentario.send_keys(Keys.RETURN)
            time.sleep(1)

            try:
                driver.find_element_by_class_name('gxNyb')
                print('\n\033[0;31mParece que está bloqueando...\033[m', end=' ')
                tentativas += 1

                if tentativas > 1:
                    print('\n\033[0;31mO programa está pausado, os comentários estão bloqueados.\033[m')
                    decisao = input('\n\033[0;31mPublique uma foto e pressione enter ou digite "xau" para sair: \033[m').lower()
                    if decisao in ['xau', 'sau', 'tchau', 'xua', 'cau', 'thau']:
                        break

                print('\n\033[0;31mTentando de novo.\033[m')
                time.sleep(10)
                problemas += 1
                continuar = False

            except:
                pass

            if continuar:
                tentativas = 0
                time.sleep(random.randint(15, 22))
                pessoas_no_comentario.clear()
                qtsjafoi += 1
                print(qtsjafoi, 'comentários')
                if qtsjafoi == qts_comments:
                    sair = True
                
        except:
            print('\n\033[0;31mParece que está bloqueando...\033[m', end=' ')
            tentativas += 1

            if tentativas > 1:
                print('\n\033[0;31mO programa está pausado, os comentários estão bloqueados.\033[m')
                decisao = input(
                    '\n\033[0;31mPublique uma foto e pressione enter ou digite "xau" para sair: \033[m').lower()
                if decisao in ['xau', 'sau', 'tchau', 'xua', 'cau', 'thau']:
                    break

            print('\n\033[0;31mTentando de novo.\033[m')
            problemas += 1
            time.sleep(10)


if __name__ == '__main__':
    data = f"{date.today().day}/{date.today().month}/{date.today().year}"
    hora_inicio = datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%H:%M:%S")

    main(usuario, senha, qts_comments, pessoas_por_comment, link, aleatorio, texto)

    hora_fim = datetime.now().astimezone(timezone("America/Sao_Paulo")).strftime("%H:%M:%S")

    hora_seg_inicio = hora_inicio.split(":")
    hora_seg_fim = hora_fim.split(":")

    contar = 0

    for parte in hora_seg_inicio:
        if contar == 0:
            segundos_inicio = int(parte) * 3600
            contar += 1
        elif contar == 1:
            segundos_inicio += int(parte) * 60
            contar += 1
        elif contar == 2:
            segundos_inicio += int(parte)
            contar += 1

    contar = 0

    for parte in hora_seg_fim:
        if contar == 0:
            segundos_fim = int(parte) * 3600
            contar += 1
        elif contar == 1:
            segundos_fim += int(parte) * 60
            contar += 1
        elif contar == 2:
            segundos_fim += int(parte)
            contar += 1

    data_fim = f"{date.today().day}/{date.today().month}/{date.today().year}"
    dias = int(data_fim.split("/")[0]) - int(data.split('/')[0])
    if segundos_fim >= segundos_inicio:
        duracao = segundos_fim - segundos_inicio
        if dias > 0:
            duracao += dias * 3600 * 24
    elif segundos_fim < segundos_inicio:
        duracao = (segundos_fim) + ((24 * 3600) - segundos_inicio)
        if dias > 1:
            duracao += (dias - 1) * 3600 * 24
    duracao = stopwatch(duracao)

    with open(relatorio, "a+") as info:
        info.write(f"No dia {data}, houveram {qtsjafoi} marcações pela conta de @{usuario}. {problemas} erros."
                   f" Início: {hora_inicio}"
                   f" {data}. Fim: {hora_fim} {data_fim}. Duração: {duracao}. Último contatado: {ultimo_marcado}."
                   f" Base de dados: {arq}\n\n")
