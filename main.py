# main.py
import sqlite3
import subprocess
import os


def buscar_usuario(user_id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # SQL INJECTION: dado externo direto na query
    query = "SELECT * FROM users WHERE id=" + user_id
    cursor.execute(query)
    return cursor.fetchone()


def executar_comando(cmd):
    # COMMAND INJECTION: shell=True com dado externo
    resultado = subprocess.check_output(cmd, shell=True)
    return resultado


def ler_arquivo(nome_arquivo):
    # PATH TRAVERSAL: caminho externo sem sanitização
    caminho = "/var/data/" + nome_arquivo
    with open(caminho, 'r') as f:
        return f.read()


if __name__ == "__main__":
    # Fonte externa: input do usuário (source reconhecido pelo CodeQL)
    user_id = input("Digite o ID: ")
    cmd = input("Digite o comando: ")
    arquivo = input("Digite o arquivo: ")

    # Fluxo direto: source -> sink (sem sanitização no meio)
    print(buscar_usuario(user_id))
    print(executar_comando(cmd))
    print(ler_arquivo(arquivo))