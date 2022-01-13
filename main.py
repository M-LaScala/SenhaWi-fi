# Enconding
# https://docs.python.org/3/library/codecs.html

# Biblioteca para conseguir usar o prompt no python
from datetime import datetime
import subprocess

# Criando arquivo txt
def verificarTxt(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except:
        print("Ocorreu um erro! ao abrir o arquivo")

def criarTxt(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Ocorreu um erro! ao abrir o arquivo")

#Comandos
listar_redes = ["netsh", "wlan", "show", "profiles"]

# Listas
lista_redes = []
lista_senhas = []

# Inicio programa
info_redes = subprocess.check_output(listar_redes, encoding='cp858')

# Pegar os nomes das redes
for linhas in info_redes.split('\n'):
    if "Usuários:" in linhas:
        posi = linhas.find(":")
        logins = linhas[posi+2:]
        lista_redes.append(logins)

# Pegar a senha de cada uma das redes encontradas
for nome in lista_redes:
    info_senha = subprocess.check_output(["netsh", "wlan", "show", "profile", nome, "key", "=", "clear"], encoding='cp858')
    for linhas in info_senha.split('\n'):
        if "Conteúdo da Chave" in linhas:
            posi = linhas.find(":")
            senhas = linhas[posi+2:]
            lista_senhas.append(senhas)

# Criacao de um arquivo com a rede e senha
nome_arquivo = "MinhasRedes.txt"

if verificarTxt(nome_arquivo):
    criarTxt(nome_arquivo)
    #print("Arquivo criado!")

with open(nome_arquivo, 'a') as arquivo:
    #Pega a quantidade de redes
    cont = len(lista_redes)
    arquivo.write(f"Informacoes retiradas: {datetime.today().strftime('%d-%m-%Y %H:%M:%S')}\n")
    for i in range(cont):
        arquivo.write(f"Rede: {lista_redes[i]} Senha: {lista_senhas[i]}\n")



