from typing import List
from time import sleep

from BancoPy.models.cliente import Cliente
from BancoPy.models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=============================')
    print('============ATM==============')
    print('========Hermos Bank==========')
    print('=============================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('informe os daados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('-------------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')

    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósiuto: '))
            conta.depositar(valor)

        else:
            print(f'Não foi encontrada conta com número {numero}')

    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        remetente: int = int(input('Informe o número da sua conta: '))
        conta_remetente: Conta = buscar_conta_por_numero(remetente)

        if remetente:
            destinatario: int = int(input('Informe o número da conta destino: '))
            conta_destinatario: Conta = buscar_conta_por_numero(destinatario)

            if destinatario:
                valor: float = float(input('Informe o valor da transferência.'))
                conta_remetente.transferir(conta_destinatario, valor)

            else:
                print(f'A conta destino com o número {destinatario} não foi encontrada.')

        else:
            print(f'A sua conta com o número {remetente} não foi enccontrada.')

    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('-----------------')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas.')
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
