
import os

menu = '''
   *** Banco Dio *** 
*----------------------* 
| Prescione:           |
| [1] Para depósitar   |
| [2] Para sacar       |
| [3] Para ver extrato |
| [4] Detalhe da conta |
| [5] Para sair        |
*----------------------*
'''

saldo = 0;
extrato = '';
NUMERO_SAQUE = 0;
LIMITE_SAQUE = 500;

while True:
    opcao = int(input(menu + 'Informe operação desejada: '))

# ----- area de depósito -------
    if opcao == 1:
        valor_deposito = int(input('Digite valor a depositar: '))
        saldo += valor_deposito
        os.system('cls')
        print('|-------------------------------------|')
        print(' Você depositou R$ ' + str(valor_deposito) + ' na sua conta.')
        print(' Obrigado pela preferência!\n')
        print('|-------------------------------------|')
        extrato += ('Depositou: ' + str(valor_deposito) + '\n')

# ---- area sacar ------------
    elif opcao == 2:
        valor_saque = int(input('\nDigite o valor que deseja sacar: '))

        if (NUMERO_SAQUE < 3):
            NUMERO_SAQUE += 1
            if valor_saque <= LIMITE_SAQUE:
                if valor_saque <= saldo:
                    os.system('cls')
                    print('|-------------------------------------|')
                    print('\nVocê sacou R$ ' + str(valor_saque) + ' da sua conta.')
                    print('Obrigado pela preferência!\n')
                    print('|-------------------------------------|')
                    saldo -= valor_saque

                    #Armazenar o valor de saque na variavel extrato
                    extrato += ('Sacou: ' + str(valor_saque) + '\n')
                else:
                    os.system('cls')
                    print('|-------------------------------------|')
                    print('\nSaldo insuficiente')
                    print('|-------------------------------------|')
                    continue
                    input('\nSaldo disponível: R$ ' + str(saldo))       
            else:
                os.system('cls')
                print('|-------------------------------------|')
                print('O limite máximo de saque é de R$ ' + str(LIMITE_SAQUE) + '.')
                print('|-------------------------------------|')
        else:
            os.system('cls')
            print('|----------------------------------------|')
            print(' Já completou o seu limite de saque diário.\n Será possível realizar saque só amanhã')
            print('|----------------------------------------|')
            

# ----  area ver extrato --------
    elif opcao == 3:
        os.system('cls')
        print('\n-- Extrato da conta --: \n')
        print(str(extrato))
        print('-------------------------')
        print('Saldo atual: ' + str(saldo))
        
# --- area ver detalhe da conta ----------
    elif opcao == 4:
        os.system('cls')
        print('\n--- Detalhe da conta ---\n')
        input('\nSaldo disponível: R$ ' + str(saldo))
    
# --- area de saida... ----------
    elif opcao == 5:
        print('\nObrigado pela preferência!\n')
        break

    else:
        os.system('cls')
        print('\nOperação inválida. Por favor, selecione a opção desejada.')