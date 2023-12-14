def inverter_numero(numero):

    if not isinstance(numero, int | float):
        raise ValueError("O valor de entrada da função deve ser um número")
    
    if numero == 0:
        raise ZeroDivisionError("A inversão de 0 não é definida na matemática")
    
    numero_invertido = round(1 / numero, 3)
    
    print(numero_invertido)


if __name__ == "__main__":
    try:
        inverter_numero(0)
    except ValueError as erro:
        print(f"Erro: {erro}")
    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")
    finally:
        print("Desenvolvido por Athílio Cavalcanti")
