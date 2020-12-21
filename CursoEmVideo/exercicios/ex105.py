#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as seguintes
# informações:
#   - Quantidades de notas
#   - A maior nota
#   - A menor nota
#   - A média da turma
#   - A situação (opcional)
# Adicione também as docstrings da função.


def notas(*n, sit=False):
    """
    ------------------------------------------------------------------------------
    notas(*n, sit=False)
    |   -> Função para analisar notas e situações de vários alunos.
    |
    |   :param n: uma ou mais notas dos alunos (aceita várias).
    |   :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    |   :return: dicionário com várias informações sobre a situação da turma.
    ------------------------------------------------------------------------------
    """
    dados_notas = {'Quantidade': 0,
                   'Maior_nota': 0,
                   'Menor_nota': 0,
                   'Media_turma': 0}
    maior = menor = cont = soma = 0

    for nota in n:
        soma += nota
        if cont == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        cont += 1

    dados_notas['Quantidade'] = len(n)
    dados_notas['Maior_nota'] = maior
    dados_notas['Menor_nota'] = menor
    dados_notas['Media_turma'] = soma / len(n)

    if sit:
        if dados_notas['Media_turma'] >= 7:
            dados_notas['Situação'] = 'BOA'
        elif dados_notas['Media_turma'] >= 5:
            dados_notas['Situação'] = 'RAZOÁVEL'
        else:
            dados_notas['Situação'] = 'RUÍM'

    return dados_notas


info = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(info)

