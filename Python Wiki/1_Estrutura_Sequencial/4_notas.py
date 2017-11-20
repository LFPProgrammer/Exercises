

'''
nota1=float(input("Informe uma nota:\n"))
nota2=float(input("Informe uma nota:\n"))
nota3=float(input("Informe uma nota:\n"))
nota4=float(input("Informe uma nota:\n"))


media = (nota1+nota2+nota3+nota4)/4

print("Média das notas: ", media)
'''

soma=0
max_notas=4

for i in range(4):
    nota = float(input("Informe uma nota:\n"))
    soma+=nota


media=soma/4
print("MEDIA: ",media)
