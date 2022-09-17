name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count={}

for lines in handle:
    if lines.startswith("From:"):
        continue
    #Escogemos las lineas que comienzan con from
    elif lines.startswith('From '):
        #Separamos las lineas en palabras
        line=lines.split()
        #Escogemos la posicion 5 de la linea (hora) y lo separamos por :
        hour=line[5].split(':')
        #Agregamos cada hora al diccionario de conteo
        count[hour[0]]=count.get(hour[0],0)+1
        

lst=list()

#Creamos una lista con las tuplas del diccionario y la ordenamos
for k,v in count.items():
    lst.append((k,v))

lst=sorted(lst)


#Imprimimos cada valor de hora y las veces que se repite
for hour, times in lst:
    print(hour, times)