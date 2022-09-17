fname = input('Please enter the file name:')
fh=open(fname)

for line in fh:
    nline=line.rstrip()
    print(nline)
    print(nline.upper())

