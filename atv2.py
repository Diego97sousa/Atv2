#!/usr/bin/env python
# coding: utf-8

# In[28]:


import csv


lista = list()
listj = list()

with open('coleta.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter = ',') 
    linhas = 0 
    for coluna in leitor: 
        if linhas == 0 :
            linhas += 1
        else: 
            
            print(f'\t{coluna[1]}')
            print(f'\t{coluna[0]}')
            
            linhas += 1
            lista.append(int(coluna[1]))
            linhas += 1
            listj.append(int(coluna[1]))
arq.close()
    
arquivo = open("rel_temp.txt", "a")
arquivo.write("Olá, mundo!")


soma = sum(lista)

temp_max = max(lista)
print('Temperatura mais alta ' ,temp_max, '°C')

temp_min = min(lista)
print('Temperatura mais baixa: ' ,temp_min, '°C')

temp_med = soma/(len(lista))

print('Valores totais das Temperaturas: ' , round(temp_med,2), '°C')







# In[ ]:





# In[ ]:




