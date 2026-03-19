import os
from decimal import Decimal, InvalidOperation

class CalculadoraAvancada:
    def __init__(self):
        self.historico = []

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def obter_numero(self, prompt):
        while True:
            try:
                entrada = input(prompt).replace(',', '.')
                return Decimal(entrada)
            except InvalidOperation:
                print("Erro: Entrada inválida. Digite um número real ou inteiro.")

    def calcular_porcentagem(self):
        print("\n--- Módulo de Porcentagem ---")
        base = self.obter_numero("Valor base: ")
        porcent = self.obter_numero("Porcentagem (%): ")
        
        print("\n1. Parte (X% de Y) | 2. Acréscimo (+) | 3. Desconto (-)")
        op = input("Opção: ")
        
        fator = (porcent / 100) * base
        
        if op == '1':
            res = fator
            msg = f"{porcent}% de {base} = {res}"
        elif op == '2':
            res = base + fator
            msg = f"{base} + {porcent}% = {res}"
        elif op == '3':
            res = base - fator
            msg = f"{base} - {porcent}% = {res}"
        else:
            return "Opção inválida."

        self.historico.append(msg)
        return msg

    def operacao_matematica(self):
        n1 = self.obter_numero("Primeiro número: ")
        n2 = self.obter_numero("Segundo número: ")
        
        print("\n[+] Soma | [-] Subtração | [*] Multiplicação | [/] Divisão | [^] Potência")
        op = input("Operação: ")

        operacoes = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero",
            '^': lambda x, y: x ** y
        }

        if op in operacoes:
            resultado = operacoes[op](n1, n2)
            registro = f"{n1} {op} {n2} = {resultado}"
            self.historico.append(registro)
            return registro
        return "Operação inválida."

    def exibir_historico(self):
        print("\n=== LOG DE OPERAÇÕES ===")
        if not self.historico:
            print("Vazio.")
        else:
            for idx, item in enumerate(self.historico, 1):
                print(f"[{idx:02d}] {item}")
        input("\nPressione Enter para voltar...")

    def menu(self):
        while True:
            self.limpar_tela()
            print("================================")
            print("   PYTHON MASTER CALCULATOR")
            print("================================")
            print("1. Cálculos Aritméticos")
            print("2. Porcentagem Avançada")
            print("3. Histórico Detalhado")
            print("0. Sair")
            
            escolha = input("\nSelecione: ")

            if escolha == '1':
                print(f"\n>> Resultado: {self.operacao_matematica()}")
                input("\nContinuar...")
            elif escolha == '2':
                print(f"\n>> Resultado: {self.calcular_porcentagem()}")
                input("\nContinuar...")
            elif escolha == '3':
                self.exibir_historico()
            elif escolha == '0':
                print("Sistema encerrado.")
                break

if __name__ == "__main__":
    calc = CalculadoraAvancada()
    calc.menu()