name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts={}

for lines in handle:
    line=lines.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
    #Dividomos las lineas por palabras y agregamos el segundo valor de la lista(correo) a la cuenta del diccionario
            words=line.split()
            counts[words[1]]=counts.get(words[1],0)+1
    
bigcount=0
bigword=0

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word


print(bigword,bigcount)
            
