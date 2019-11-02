print('Faça um Programa que peça as 4 notas bimestrais e mostre a média. ')

def main():
	aprovado = 60
	reprovado = 59

	_1bimestre = int(input('Digite a nota do 1 Bimestre: '))
	_2bimestre = int(input('Digite a nota do 2 Bimestre: '))
	_3bimestre = int(input('Digite a nota do 3 Bimestre: '))
	_4bimestre = int(input('Digite a nota do 4 Bimestre: '))


	soma =  _1bimestre + _2bimestre + _3bimestre + _4bimestre
	if soma >= aprovado:

		print('Aluno Aprovado:', soma)
	else:
		print('Aluno Reprovado', soma)

main()
