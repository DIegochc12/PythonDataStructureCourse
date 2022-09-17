fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh=open(fname)


count=0
for lines in fh:
    line=lines.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        count=count+1
        words=line.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
