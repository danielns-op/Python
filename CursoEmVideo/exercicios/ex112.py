#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos
# um módulo chamado dado. Crie uma funçao chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma
# validação de dados para aceitar apenas valores que sejam monetários.
from utilidadesCeV import dado, moeda

valor = dado.leiaDinheiro('Digite o preço: R$ ')

moeda.resumo(valor, 35, 22)

