import csv

from datetime import datetime, date
import csv
import matplotlib.pyplot as plt


listac=list()
listat=list()
with open('coleta.csv', mode='r', encoding='utf8') as arq:

    leitor = csv.reader(arq, delimiter=',')
    linhas = 0
    for coluna in leitor:
        if linhas == 0:
            linhas += 1
        else:
           
            
            linhas += 1
            listac.append((coluna[0]))
            linhas += 1
            listat.append(int(coluna[1]))
            
soma = sum(listat)

maior= max(listat)
print('O maior valor das temperaturas é : ',maior, 'ºC')

menor= min(listat)
print('O menor valor das temperaturas é : ',menor, 'ºC')

media = soma/(len(listat))
print('Essa é a média das temperaturas: ',round(media,2),'ºC')

hoje= date.today().strftime('%d-%m-%y')
print(hoje)

arquivo = open  ('rel_temp.dat','w')
arquivo.write("#'''''''''''''''''''''''''''''''''''''''#\n")
arquivo.write("Diego Silva de Sousa")
arquivo.write(f"\nData:{hoje}")
arquivo.write(f"\ntemperatura média:{media}")
arquivo.write(f"\ntemperatura mais alta:{maior}")
arquivo.write(f"\ntemperatura mais baixa:{menor}")
arquivo.write("\n#'''''''''''''''''''''''''''''''''''''''#")

arq.close()

x = (listac)
y = (listat)

fig, ax = plt.subplots()

ax.scatter(x, y)

ax.set_xlabel('tempo')
ax.set_ylabel('temperatura em graus')

ax.set_title('temperatura no periodo de 12 hrs')

plt.show()
