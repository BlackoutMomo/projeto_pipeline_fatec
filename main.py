# main.py

def dividir(a, b):
    return a / b


def saudacao(nome):
    return f"Olá, {nome}!"


def main():
    print(saudacao("Gabriel"))

    resultado = dividir(10, 2)

    print(f"Resultado da divisão: {resultado}")


if __name__ == "__main__":
    main()