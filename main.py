# main.py
import sqlite3


def saudacao(nome: str) -> str:
    """Retorna uma saudação segura."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    """Calcula a média de uma lista de notas."""
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)


def buscar_usuario_vulneravel(user_id):
    """⚠️ SQL INJECTION: esta função tem uma vulnerabilidade intencional!"""
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # ⚠️ SQL INJECTION: nunca faça isso em produção!
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchone()


if __name__ == "__main__":
    print(saudacao("Aluno FATEC"))
    print(f'Média: {calcular_media([8.5, 9.0, 7.5])}')
    
    # ⚠️ Esta linha vai ativar a detecção do CodeQL para SQL Injection
    user_input = input("Digite ID do usuário: ")
    resultado = buscar_usuario_vulneravel(user_input)
    print(f"Usuário encontrado: {resultado}")
