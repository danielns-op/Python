#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.
from uteis import moeda

valor = float(input('Digite o preço: R$ '))

moeda.resumo(valor, 80, 35)

