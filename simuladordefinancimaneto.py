# SIMULADOR DE financiamento
from datetime import datetime

from dateutil.relativedelta import relativedelta


def pular_linha() -> None:
    '''Salta linha na exibição do terminal'''
    print()


def validar_financ() -> int:
    '''Função retorna o valor do financiamento que o usuário necessita. \n
        Permite apenas entrada de números inteiros diferentes de 0 '''
    while True:
        valor = input('\033[47;1;32mQual vai ser o valor do financiamento?:')
        if valor.isnumeric() and valor != '0':
            valor = int(valor)

            pular_linha()
            print(f'O valor do financiamento será R$ {valor:,.2f}')
            pular_linha()

            return valor
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


def soma_60days() -> datetime:
    '''Função que retorna a data da primeira parcela do financiamento.\n
        datetime.now() que representa 'data de hoje' somado a relativedelta
            (days=60) que representa '60dias'.\n
                Permite apenas entrada de números inteiros. '''

    primeira_parcela = datetime.now() + relativedelta(days=60)

    print(f'A primeira parcela será paga só daqui a 60 dias '
          f'({primeira_parcela.strftime("%d/%m/%Y")})')
    pular_linha()

    return primeira_parcela


def qtd_p_valida() -> int:
    '''Função que retorna a quantidade de prestacoes que o usuário
        deseja para pagar o financiamento. \n
            Permite apenas entrada de números inteiros maiores do que
              0 e menores ou iguais a 60 (que é  a quantidade máxima permitida)
    '''
    print(f'Você pode parcelar o valor de {valor_i:,.2f}'
          f' em até 60 vezes com uma taxa de juros de 3,5% ao mês')
    while True:
        valor = input(
            ('\033[47;1;32mDigite a quantidade de prestações desejada: '))
        if valor.isnumeric():
            valor = int(valor)
            if valor > 0 and valor <= 60:
                return valor
            else:
                print(
                    '\033[31mERRO! Digite uma quantidade de prestacoes válida '
                    '(MIN 1/ MAX 60)\033[m')
        else:
            print('\033[31mERRO! Digite um número válido\033[m')
            pular_linha()


def exibir_simulacao(data_inicial: datetime, data_final: datetime):
    '''Função que recebe como parâmetros a data que o usuário pegou
        o financiamento e a data da ultima parcela.\n
            E exibe no terminal o resumo da operação  '''
    tot_prestacoes = []
    ''' lista que vai armazenar as datas das prestações'''
    while data_inicial < data_final:
        tot_prestacoes.append(data_inicial)
        data_inicial += relativedelta(months=1)

    pular_linha()
    print('-'*52)
    print(f"{'#':<2}{'Data':>20}{'Pagamento':>25}")
    for n, data in enumerate(tot_prestacoes):
        print(
            f"{n+1:<2}{data.strftime('%d/%m/%Y'):>23}{prestacao:>21.2f}")
    print('-'*52)

    pular_linha()
    print(
        f'Quantidade de prestacoes = {qtd_p} \n'
        f'Valor das prestacoes = R${prestacao:.2f} \n'
        f'Valor final do financiamento R${valor_final:.2f} \n'
        f'Sendo R${j_aplicados:.2f} juros')
    pular_linha()
    print(
        'A primeira parcela será paga em '
        f'{primeira_parcela.strftime("%d/%m/%Y")} e a ultima em '
        f'{ultima_parcela.strftime("%d/%m/%Y")}')


if __name__ == '__main__':
    valor_i = validar_financ()

    primeira_parcela = soma_60days()

    qtd_p = qtd_p_valida()

    j = 0.035
    '''Valor Médio de juros cobrado por financiamento no Brasil'''

    prestacao = valor_i * (((1+j)**qtd_p) * j) / (((1+j)**qtd_p) - 1)
    '''Valor das prestacoes após aplicar os juros e amortizar no sistema'price'
        https://www.suno.com.br/artigos/tabela-price/'''

    valor_final = prestacao * qtd_p
    '''Valor final que será pago pelo financiamento após
        aplicação da taxa de juros'''

    j_aplicados = valor_final - valor_i
    '''recebe o valor dos juros aplicados no valor financiado'''

    ultima_parcela = primeira_parcela + relativedelta(months=qtd_p)
    '''variável 'ultima_parcela' recebe a variável 'primeira_parcela' somada a
        quantidade de meses que o usuário optou para fazer o parcelamento'''

    exibir_simulacao(primeira_parcela, ultima_parcela)
