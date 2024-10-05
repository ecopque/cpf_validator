import re
import sys

entrada = input('Digite um CPF: ')
cpf_usuario = re.sub(r'[^0-9]', '', entrada) # peneira

repeticao = entrada == entrada[0] * len(entrada)
if repeticao is True:
   print('Você repetiu alguns caracteres.')
   sys.exit()

nove_digitos = cpf_usuario[:9]
contagem_regressiva = 10
hd_soma = 0
for numero in nove_digitos:
   hd_soma += int(numero) * contagem_regressiva
   contagem_regressiva -= 1
resto_div = (hd_soma * 10) % 11
resultado = resto_div if resto_div <= 9 else 0

dez_digitos = nove_digitos + str(resultado)
contagem_regressiva2 = 11
hd_soma2 = 0
for numero2 in dez_digitos:
   hd_soma2 += int(numero2) * contagem_regressiva2
   contagem_regressiva2 -= 1
resto_div2 = (hd_soma2 * 10) % 11
resultado2 = resto_div2 if resto_div2 <= 9 else 0

novo_cpf = f'{nove_digitos}{resultado}{resultado2}'
print(f'Primeiro dígito: {resultado}. Segundo dígito: {resultado2}.')
if cpf_usuario == novo_cpf:
   print(f'CPF: {cpf_usuario} é válido.')
else:
   print(f'CPF: {cpf_usuario} é inválido.')

# https://linktr.ee/edsoncopque
