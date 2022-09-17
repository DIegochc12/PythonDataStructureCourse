fname=input("Please enter the file name:")
fh=open(fname,'r')
cnt=0
numb=0
sm=0
avg=0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue 

    cnt=cnt+1
    x=line.find(':')
    x2=line[x+1:]
    numb=float(x2.rstrip())
    sm=sm+numb


avg=sm/cnt
print("Average spam confidence:",avg)
print("Done :)")


