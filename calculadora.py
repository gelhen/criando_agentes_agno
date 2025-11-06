def exibir_menu() -> None:

    print("\n=== Calculadora Simples ===")
    print("1) Adição (+)")
    print("2) Subtração (-)")
    print("3) Multiplicação (*)")
    print("4) Divisão (/)")
    print("5) Exponenciação (**)")
    print("6) Divisão inteira (//)")
    print("7) Módulo (%)")
    print("0) Sair")


def ler_numero(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()
        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida. Digite um número válido (ex.: 10, 3.14, -2).")



def calcular(operacao: str, a: float, b: float) -> float:
    if operacao == "+":
        return a + b
    if operacao == "-":
        return a - b
    if operacao == "*":
        return a * b
    if operacao == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b
    if operacao == "**":
        return a ** b
    if operacao == "//":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a // b
    if operacao == "%":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a % b
    raise ValueError("Operação desconhecida.")


def main() -> None:
    mapa_opcoes = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "**",
        "6": "//",
        "7": "%",
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo... Até mais!")
            break

        operacao = mapa_opcoes.get(opcao)
        if not operacao:
            print("Opção inválida. Tente novamente.")
            continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        try:
            resultado = calcular(operacao, a, b)
            simbolo = operacao
            print(f"Resultado: {a} {simbolo} {b} = {resultado}")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()


