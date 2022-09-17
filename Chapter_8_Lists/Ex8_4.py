fname=input("Enter the file name:")
fh=open(fname,'r')
lst=list()
for line in fh:
    #print(line.rstrip())
    pieces=line.split()

    for word in pieces:
        if word not in lst:
            lst.append(word)

lst.sort()

print(lst)
